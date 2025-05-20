from flask import Flask, request
import requests
import json

app = Flask(__name__)

# تحميل قاعدة المعرفة
with open('knowledge.json', 'r', encoding='utf-8') as f:
    knowledge_base = json.load(f)

BOT_TOKEN = 'ضع_التوكن_الجديد_هنا'
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    if 'message' in data and 'text' in data['message']:
        chat_id = data['message']['chat']['id']
        user_message = data['message']['text'].strip()

        # البحث في قاعدة المعرفة
        reply = knowledge_base.get(user_message, "عذراً، لا توجد إجابة لهذا السؤال حالياً.")

        # إرسال الرد
        requests.post(API_URL, json={
            'chat_id': chat_id,
            'text': reply
        })

    return 'OK', 200

if __name__ == '__main__':
    app.run()