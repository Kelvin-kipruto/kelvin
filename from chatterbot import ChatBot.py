from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chatbot
bot = ChatBot('MyChatBot')
# Train the bot using a list of conversation
trainer = ListTrainer(bot)
trainer.train([
    'Hi',
    'Hello',
    'How are you?',
    'I am doing great.',
    'That is good to hear.',
    'Thank you',
    'You are welcome.',
    'What is your name?',
    'My name is MyChatBot.'
])

# Start the conversation
while True:
    user_input = input('You: ')
    bot_response = bot.get_response(user_input)
    print('Bot:', bot_response)