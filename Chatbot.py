### import liraries 
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.response_selection import get_most_frequent_response
from chatterbot.trainers import ChatterBotCorpusTrainer
import os


bot=ChatBot('Prisma')#,        ### Create a new bot,chatbot
           # logic_adapters=[
            #'chatterbot.logic.BestMatch',
          #  'chatterbot.logic.MathematicalEvaluation'],
          #  response_selection_method=get_most_frequent_response,

trainer = ListTrainer(bot)       ## add trainer for your bot


#training and tolking bor
for files in os.listdir('./libery'):
    data=open('./libery/'+files,'r').readlines()  ##My libery for bot understend
    trainer.train(data)         #chat feature
while True:
    message=input('You: ')
    
    if message.strip()!='Bye':
        reply=bot.get_response(message)
        print('Prisma:',reply)
    
    if message.strip()=='Bye':
        print('Prisma: Bye')
        break