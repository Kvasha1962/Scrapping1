import csv

from bs4 import BeautifulSoup

with open("index.html", encoding="utf-8") as f:
    html_text = f.read()

bs: BeautifulSoup = BeautifulSoup(html_text, "lxml")

first_header = (
    bs.find("div", class_="table-responsive bg-white mt-3")
    .find("tr", class_="fon-table-deepgreen py-3")
    .find("span", class_="h6 text-white")
)
first_header_text: str = first_header.text
list_first_header: list = [first_header_text]

second_header = bs.find("div", class_="table-responsive bg-white mt-3").find(
    "tr", class_="fon-table-lightgreen"
)

third_header = bs.find("div", class_="table-responsive bg-white mt-3").find(
    "tr", class_="fon-table-midgreen py-3"
)

table_first = (
    bs.find("div", class_="table-responsive bg-white mt-3")
    .find("table", class_="table table-bordered")
    .find("tbody")
    .find_all("td")
)

list_first_table = list()
list_first_table_temp = list()

for j in table_first:
    if j.text.strip() != "":
        list_first_table.append(j.text.strip())

count = 1
list_first_table_new = list()
list_first_table_new_temp = list()

for i in list_first_table:
    if count < 3:
        list_first_table_new_temp.append(i)
        count += 1
    elif count == 3:
        list_first_table_new_temp.append(i)
        list_first_table_new.append(list_first_table_new_temp)
        list_first_table_new_temp = list()
        count = 1

list_first_table = list()
for i in list_first_table_new:
    list_first_table.append(i)

third_header_text: str = third_header.text
list_third_header: list = [third_header_text]

dict_second_header_new = {}
i = 1

for column in second_header:
    if column.text.strip() != "Продукт":
        dict_second_header_new[i] = column.text.strip()
        i += 1
dict_second_header_new.pop(1)
dict_second_header_new.pop(5)

with open("header.csv", "w", encoding="utf-8", newline="") as f:
    header = csv.writer(f)
    header.writerow(list_first_header)
    header.writerow(dict_second_header_new.values())
    header.writerow(list_third_header)
    header.writerows(list_first_table)
