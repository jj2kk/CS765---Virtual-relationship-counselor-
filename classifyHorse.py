import json

def main():
    phrases = readPhrases()


def readPhrases():
    filename = input("please enter filename: ")
    with open(filename+'.json', 'r') as f:
        try:
            data = json.load(f)
        # if the file is empty the ValueError will be thrown
        except ValueError:
            data = {}
    data = dict(data)
    for key in data.iterkeys():
        key = int(key)

def classify_text():

    print(data)
    print(data[1])




main()