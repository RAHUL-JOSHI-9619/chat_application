from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory list to store messages (temporary storage)
messages = []

@app.route('/')
def index():
    # Render the chat page with the current list of messages
    return render_template('chat.html', messages=messages)

@app.route('/send_message', methods=['POST'])
def send_message():
    # Get the message from the frontend form and append it to the messages list
    message = request.form.get('message')
    if message:
        messages.append(message)
    return '', 204  # Respond with no content (successful)

@app.route('/get_messages')
def get_messages():
    # Return the list of messages as a JSON response
    return jsonify(messages)

@app.route('/clear_chat', methods=['POST'])
def clear_chat():
    # Clear the messages list
    messages.clear()
    return '', 204  # Respond with no content (successful)

if __name__ == '__main__':
    app.run(debug=True)
