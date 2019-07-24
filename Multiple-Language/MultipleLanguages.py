import json

language = "russian.json"
language = "english.json"

with open(language) as lang:
    dictionary = json.load(lang)


print("This is greeting")
print(dictionary["greetings"])

print("Main Menu")
print(dictionary["menu1_text"])
