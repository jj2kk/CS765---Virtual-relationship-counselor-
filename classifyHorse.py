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
    f.close()

def classify_text():
    personA = [0,0,0,0]
    personB = [0,0,0,0]
    filename = input("please enter filename: "+"txt")
    for lines in filename:
        '''
        Assign each line to a person
        evaluate each line and update the person's score for each horseman
        '''





main()