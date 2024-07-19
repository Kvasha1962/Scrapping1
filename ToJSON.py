import json

from ToCSV import list_first_table

keys = ["name", "gi", "description"]
general_json = dict()
k = 1
for item_list in list_first_table:
    dict_item = dict(zip(keys, item_list))
    general_json[k] = dict_item
    k += 1

with open("ExJSON.json", "w", encoding="utf-8") as f:
    json.dump(general_json, f, indent=2, ensure_ascii=False)
