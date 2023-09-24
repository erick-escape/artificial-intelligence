from view import sense, act
import json
import random


def runRobot():
    stt = sense.speech_to_text()
    print('STT = ', stt)

    with open('./model/dataset.json', 'r', encoding="utf8") as file:
        dataset = json.loads(file.read())
        for word in stt:
            if word in dataset['cumprimentos']:
                act.act(random.choice(dataset['resCumprimentos']))
                break
            elif word in dataset['supinos']:
                act.act(dataset['resSupinos'])
                break
            elif word in dataset['puxadas']:
                act.act(dataset['resPuxadas'])
                break
            elif word in dataset['remadas']:
                act.act(dataset['resRemadas'])
                break
            elif word in dataset['agachamentos']:
                act.act(dataset['resAgachamentos'])
                break
            elif word in dataset['roscas']:
                act.act(dataset['resRoscas'])
                break
            elif word in dataset['triceps']:
                act.act(dataset['resTriceps'])
                break
            elif word in dataset['despedidas']:
                act.act(random.choice(dataset['resDespedidas']))
                break
