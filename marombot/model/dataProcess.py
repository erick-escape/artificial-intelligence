from view import act
import json
import random


def readFile(stt):
    with open('./dataset.json', 'r', encoding="utf8") as file:
        dataset = json.loads(file.read())
        for word in stt:
            if word in dataset['cumprimentos']:
                return random.choice(dataset['resCumprimentos'])
            elif word in dataset['supinos']:
                return dataset['resSupinos']
            elif word in dataset['puxadas']:
                return dataset['resPuxadas']
            elif word in dataset['remadas']:
                return dataset['resRemadas']
            elif word in dataset['agachamentos']:
                return dataset['resAgachamentos']
            elif word in dataset['roscas']:
                return dataset['resRoscas']
            elif word in dataset['triceps']:
                return dataset['resTriceps']
            elif word in dataset['despedidas']:
                return random.choice(dataset['resDespedidas'])
