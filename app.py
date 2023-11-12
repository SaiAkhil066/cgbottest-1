from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def chatbot():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot_response():
    user_message = request.json['message'].lower()
    response = get_response(user_message)
    return jsonify({"message": response})

def get_response(user_message):
    if user_message == 'hi':
        return 'Hello! How can I assist you?'
    elif user_message == 'how are you':
        return 'Iam Good. May I know about you. and How can I help you please?'
    elif user_message == 'bye':
        return 'Goodbye! Feel free to come back anytime.'
    elif user_message == 'thankyou':
        return 'The pleasure is mine, come back with the great spirit like always you do.'
    else:
        return "I'm not sure how to answer that. Please ask another question or else get back with the correct spelling."

if __name__ == '__main__':
    app.run(debug=True)
