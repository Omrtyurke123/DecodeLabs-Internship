# project 1 - chat bot 
def chat(text):
    data ={
        'hi' : ['hi','hello','welcom'],
        'bye' : ['bye','goodbye',],
        'name' : ['your name','what is your name',]
    }
    while True:
        if text in data['hi']:
            print('hi')
        elif text in data['name']:
            print('Ai chatbot')
        elif text in data['bye']:
            print('bye')
        elif text == 'exit':
            print()