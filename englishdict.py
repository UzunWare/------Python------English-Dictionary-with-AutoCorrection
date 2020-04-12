import pandas as pd
import json

data = json.load(open("data2.json"))

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def autoCorrect(key):
    for datakey in data.keys():
        k = datakey
        siz1 = len(k)
        siz2 = len(key)
        if siz1 > siz2:
            siz = siz2
            if siz1 - siz2 >= 2:
                continue
        else:
            siz = siz1
            if siz2 - siz1 >= 2:
                continue
        if key[0] != k[0]:
            continue
        count = 0
        for i in range(siz):
            if key[i] in k[i]:
                count += 1
                k.replace(key[i], '')
        if count >= siz2 / 2:
            print("Did you mean '{}'. Press 'Y' or 'N' : ".format(datakey))
            ans = input()
            if ans == 'Y':
                return datakey
    return 'none'


def getTheMeaning(key):
    if key in data.keys():
        return data[key]
    else:
        return "The word is not exist. Please double check it."


if __name__ == "__main__":
    while True:
        key = input("Enter a word (\e for exit): ")
        key = key.lower()
        if key == '\e':
            break
        if key not in data.keys():
            key = autoCorrect(key)
            if key == 'none':
                "Word is not exist. Please double check it..."
                continue
        meaning = getTheMeaning(key)
        meaning = str(meaning)
        meaning = meaning.replace("['", "")
        meaning = meaning.replace("']", "")
        meaning = meaning.replace("', ", "\n")
        meaning = meaning.replace("'", "")
        key = key.title()
        print(color.BOLD + "{} : ".format(key) + color.END,
              color.RED + meaning + color.END)