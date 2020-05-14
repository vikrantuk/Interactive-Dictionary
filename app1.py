import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    elif word.capitalize() in data:
        return data[word.capitalize()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        li = get_close_matches(word,data.keys(),n=1,cutoff=0.8)
        if(len(li)>0 and input(f"Did you mean {li[0]}? y/n: ").lower()=='y'):
            return data[li[0]]
        else:
            return ["Word doesn't exist. Please check the word again..!"]

word = input("Enter word: ").lower()

print(*translate(word),sep="\n")
