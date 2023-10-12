from view import sense
from model import dataProcess
from view import act
import json


def runRobot():
    stt = sense.speech_to_text()
    print('STT = ', stt)
    speech = dataProcess.readFile(stt)
    act.act(speech)
    with open('./dataset.json', 'r', encoding="utf8") as file:
        dataset = json.loads(file.read())
        if (speech in dataset['resDespedidas']):
            return False
        else:
            return True
