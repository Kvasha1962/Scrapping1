import csv

from bs4 import BeautifulSoup

with open("index.html", encoding="utf-8") as f:
    html_text = f.read()

bs: BeautifulSoup = BeautifulSoup(html_text, "lxml")

first_header: BeautifulSoup = (
    bs.find("div", class_="table-responsive bg-white mt-3")
    .find("tr", class_="fon-table-deepgreen py-3")
    .find("span", class_="h6 text-white")
)
first_header_text: str = first_header.text
list_first_header: list = [first_header_text]

second_header: BeautifulSoup = bs.find(
    "div", class_="table-responsive bg-white mt-3"
).find("tr", class_="fon-table-lightgreen")

print(first_header.text)

dict_second_header: dict = {}

third_header: BeautifulSoup = bs.find(
    "div", class_="table-responsive bg-white mt-3"
).find("tr", class_="fon-table-midgreen py-3")

third_header_text: str = third_header.text
list_third_header: list = [third_header_text]


for column in second_header:
    print(column.text.strip(), end="  ")
    if column.text.strip():
        dict_second_header[column.text.strip()] = column.text.strip()

print(dict_second_header)

with open("header.csv", "w", encoding="utf-8", newline="") as f:
    header = csv.writer(f)
    header.writerow(list_first_header)
    header.writerow(dict_second_header.keys())
    header.writerow(list_third_header)
