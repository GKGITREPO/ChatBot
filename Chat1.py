import random
import json
import torch
from model import NeuralNet


def input_process (user_input):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    with open('intents.json', 'r') as json_data:
        intents = json.load(json_data)

        FILE = "data.pth"
        data = torch.load(FILE)
        input_size = data["input_size"]
        hidden_size= data["hidden_size"]
        output_size = data[ "output_size"]
        all_words = data[ 'all_words']
        tags = data["tags"]
        model_state = data["model_state"]

        model = NeuralNet (input_size, hidden_size, output_size).to(device)
        model.load_state_dict(model_state)
        model.eval()

#bot_name = "Ash"
        print("Let's chat! (type 'quit' to exit)")
        while True:
            #sentence
            # input("You: ")
            sentence = user_input
            sentence = tokenize(sentence)
            print (sentence)
            print (all_words)
            X = bag_of_words (sentence, all_words)
            print(X)
            X = X.reshape(1, X.shape[0])
            print(X)
            X = torch.from_numpy (X).to(device)
            output= model (X)
            _, predicted = torch.max(output, dim=1)
            tag = tags [predicted.item()]

            probs = torch.softmax(output, dim=1)
            prob = probs[0] [predicted. item()]
            if prob.item() > 0.75:
                for intent in intents['intents']:
                    if tag== intent["tag"]:
                        #print (f" (bot_name): (random.choice (intent['responses'])}")
                        return random.choice(intent['responses'])
            else:
                #print(f" (bot_name): I do not understand...")
                return "I do not understand..."