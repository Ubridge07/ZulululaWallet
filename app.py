from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def whatsapp():
    incoming_msg = request.values.get('Body', '').strip().lower()
    resp = MessagingResponse()
    msg = resp.message()

    if incoming_msg in ['hi', 'hello', 'help']:
        msg.body("📌 *Zululula Wallet Commands:*\n1. Borrow\n2. Lend\n3. Donate\n4. My Account\n5. Send Money")
    elif incoming_msg == '1':
        msg.body("*Borrow:* 1. 1,000\n2. 2,000\n3. 5,000\n4. 10,000\n5. 20,000\n6. 50,000\n7. Other")
    elif incoming_msg == '2':
        msg.body("*Lend:* 1. 1,000\n2. 2,000\n3. 5,000\n4. 10,000\n5. 20,000\n6. 50,000\n7. Other")
    elif incoming_msg == '3':
        msg.body("*Donate:* 1. Individual\n2. Group\n3. NGO\n4. Other")
    elif incoming_msg == '4':
        msg.body("*My Account:* 1. Balance\n2. Transactions\n3. Loans\n4. Deposit")
    elif incoming_msg == '5':
        msg.body("*Send Money:* 1. Individual\n2. Vendor")
    else:
        msg.body("❓ I didn’t understand that. Type *Hi* to see the main menu.")

    return str(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)