# project 1 - chat bot 
def chat():
    data ={
        'hi' : ['hi','hello','welcom'],
        'bye' : ['bye','goodbye'],
        'name' : ['your name','what is your name']
    }
    while True:
        text = input().lower().strip()
        if text in data['hi']:
            print('hi')
        elif text in data['name']:
            print('Ai chatbot')
        elif text in data['bye']:
            print('bye')
            break
        elif text == 'exit':
            print('bye')
            
        else:
            print('chatbot not understand this text')
    
chat()