from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Set up the chatbot
class SimpleChatBot:
    def __init__(self):
        self.chatbot = ChatBot(
            'EmpireGPT',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            logic_adapters=[
                'chatterbot.logic.BestMatch',
                'chatterbot.logic.MathematicalEvaluation'
            ]
        )
        
        # Train the bot with the English corpus
        trainer = ChatterBotCorpusTrainer(self.chatbot)
        trainer.train('chatterbot.corpus.english')

    def get_response(self, user_input):
        # Check for specific questions and respond accordingly
        if 'what model are you' in user_input.lower():
            return "I am EmpireGPT, an AI created by Empire Tech."
        
        # If no specific match, return the chatbot's regular response
        return self.chatbot.get_response(user_input)
      
