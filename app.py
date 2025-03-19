from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dummy trait data, or the actual logic you use for analysis
traits = {
    'Assertive': 0,
    'Competitive': 0,
    'Cooperative': 0,
    'Passive': 0,
    'PassiveAggressive': 0,
    'agreeableness': 0,
    'anger': 0,
    'attractiveness': 0,
    'confidence': 0,
    'conscientiousness': 0,
    'disgust': 0,
    'extraversion': 0,
    'extrovert': 0,
    'fear': 0,
    'feeling': 0,
    'formality': 0,
    'happiness': 0,
    'intelligence': 0,
    'interest': 0,
    'introvert': 0,
    'intuitive': 0,
    'judging': 0,
    'listening_skills': 0,
    'neuroticism': 0,
    'openness_to_Experience': 0,
    'perceiving': 0,
    'promiscuous': 0,
    'sadness': 0,
    'sense_of_humor': 0,
    'sensitive': 0,
    'status': 0,
    'stress_level': 0,
    'surprise': 0,
    'thinking': 0,
    'language': 0
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    
    # Simulating chatbot response based on input
    if "traits" in user_input.lower():
        response = "Here are the current traits: " + str(traits)
    else:
        response = "I'm sorry, I didn't understand that. Could you tell me more?"

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
