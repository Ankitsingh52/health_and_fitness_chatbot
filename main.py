import random

# Define the knowledge base
knowledge_base = {
    'greetings': [
        'Hi there! How can I assist you with your health and fitness goals?',
        'Hello! I\'m here to help you achieve your health and fitness goals. What do you need assistance with?'
    ],
    'workout_advice': [
        'For a great cardio workout, try jogging or biking for at least 30 minutes a day!',
        'For strength training, consider doing squats, lunges, and pushups to build muscle and tone your body.'
    ],
    'nutrition_advice': [
        'Eating a balanced diet of fruits, vegetables, lean proteins, and whole grains is key to a healthy lifestyle.',
        'To boost your energy and keep you feeling full, try eating foods that are high in fiber and protein.'
    ],
    'water_intake': [
        'To stay hydrated, aim to drink at least 8-10 cups of water per day.',
        'Drinking water can help with weight loss, digestion, and keeping your body functioning properly.'
    ]
}

# Define a function to handle user input and generate bot responses
def chatbot_response(user_input):
    response = ''
    # Check if user input matches a known intent
    for intent, phrases in knowledge_base.items():
        if user_input in phrases:
            response = random.choice(knowledge_base[intent])
            break
    # If no intent was matched, provide a default response
    if response == '':
        response = 'I\'m sorry, I didn\'t understand. Can you please rephrase your question?'
    return response

# Define a main function to handle the chat loop
def main():
    print('Welcome to the Health and Fitness Chatbot! How can I assist you today?')
    while True:
        # Get user input
        user_input = input('> ')
        # Generate bot response
        bot_response = chatbot_response(user_input)
        # Print bot response
        print(bot_response)

# Call the main function to start the chat loop
if __name__ == '__main__':
    main()
