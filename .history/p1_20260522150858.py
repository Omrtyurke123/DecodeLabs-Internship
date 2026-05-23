# project 1 - chat bot 
def chat():
    data ={
        'hi' : ['hi','hello','welcom'],
        'bye' : ['bye','goodbye'],
        'name' : ['your name','what is your name']
    }
    while True:
        text = input('you : ').lower().strip()
        if text in data['hi']:
            print('chatbot : hi')
        elif text in data['name']:
            print('chatbot : Ai chatbot')
        elif text in data['bye']:
            print('chatbot : bye')
            break
        elif text == 'exit':
            print('chatbot : bye')
            
        else:
            print('chatbot : fchatbot not understand this text')
    
chat()