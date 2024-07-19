import json

dict_example = [
    {"one": "one", "two": "two", "three": "three"},
    {"four": "four", "five": "five", "six": "six"},
    {
        "seven": "seven",
        "eight": "eight",
        "nine": "nine",
        "ten": "ten",
    },
]
pjson = json.dumps(dict_example, indent=2)
print(pjson)

with open("ExJSON.json", "w") as f:
    json.dump(dict_example, f, indent=2)
