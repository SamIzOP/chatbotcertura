from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# Dictionary of questions and responses (FAQ database), some default responses, nothing special.
chatbot_responses = {
    # Greetings
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! What can I do for you?",
    "hey": "Hey! How can I assist you?",
    "good morning": "Good morning! How can I help you?",
    "good afternoon": "Good afternoon! What can I do for you?",
    "good evening": "Good evening! How can I assist you?",
    
    # Common questions
    "what is your name": "I'm a simple chatbot created to help answer your questions!",
    "who are you": "I'm a chatbot designed to assist you with various questions.",
    "how are you": "I'm doing well, thank you for asking! How can I help you?",
    "what can you do": "I can answer questions, provide information, and have a conversation with you!",
    
    # FAQ examples
    "what are your hours": "We're open Monday through Friday, 9 AM to 5 PM.",
    "how do i contact support": "You can contact support by emailing support@example.com or calling (555) 123-4567.",
    "what is the weather": "I don't have access to current weather data, but you can check a weather website or app!",
    "how do i reset my password": "To reset your password, click on 'Forgot Password' on the login page and follow the instructions.",
    "where are you located": "We're located at 123 Main Street, City, State 12345.",
    
    # Goodbye
    "bye": "Goodbye! Have a great day!",
    "goodbye": "Goodbye! Feel free to come back anytime!",
    "see you later": "See you later! Take care!",
    "thanks": "You're welcome! Is there anything else I can help you with?",
    "thank you": "You're very welcome! Happy to help!"
}

# fallback responses
fallback_responses = [
    "I'm sorry, I don't understand that question. Could you try rephrasing it?",
    "I'm not sure about that. Can you ask me something else?",
    "That's an interesting question, but I don't have an answer for it right now.",
    "I don't have information about that topic. Is there something else I can help you with?",
    "Could you please rephrase your question? I'd like to help but I'm not sure what you're asking."
]

def preprocess_input(user_input):
    """Clean and preprocess user input"""
    # Convert to lowercase and strip whitespace
    processed = user_input.lower().strip()
    
    # Remove punctuation at the end
    processed = re.sub(r'[.!?]+$', '', processed)
    
    return processed

def get_response(user_input):
    """Get chatbot response based on user input"""
    processed_input = preprocess_input(user_input)
    
    # Check for exact matches first
    if processed_input in chatbot_responses:
        return chatbot_responses[processed_input]
    
    # Check for partial matches (keywords)
    for key in chatbot_responses:
        if key in processed_input or processed_input in key:
            return chatbot_responses[key]
    
    # If no match found, return a random fallback response
    import random
    return random.choice(fallback_responses)

@app.route('/')
def home():
    """Serve the main chatbot interface"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat requests"""
    user_message = request.json.get('message', '')
    
    if not user_message:
        return jsonify({'response': 'Please enter a message!'})
    
    bot_response = get_response(user_message)
    
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
