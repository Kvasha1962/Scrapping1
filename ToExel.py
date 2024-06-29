import xlsxwriter

from ToCSV import (
    list_first_header,
    dict_second_header_new,
    list_first_table,
    list_third_header,
    )

for item in list_first_table:
    for i in item:
        try:
            index = item.index(i)
            i = int(i)
            item[index] = i
        except ValueError:
            pass

list_second_header = [item for item in dict_second_header_new.values()]

workbook = xlsxwriter.Workbook("Glick2.xlsx")
worksheet = workbook.add_worksheet("Гликемический индекс")
worksheet.set_column("B:D", 9)
worksheet.set_row(1, 120)
worksheet.set_column(1, 300)


def mergeFormat(bold, align, valign, color, fontSize):
    merge_format = workbook.add_format(
        {
            "bold": bold,
            "align": align,
            "valign": valign,
            "color": color,
            "font_size": fontSize,
        }
    )
    return merge_format


worksheet.merge_range(
    "B2:D2", list_first_header[0], mergeFormat(1, "center", "vcenter", "red", 24)
)

worksheet.merge_range(
    3,
    1,
    3,
    3,
    list_third_header[0],
    mergeFormat(1, "center", "vcenter", "green", 14),
)

worksheet.write_row(
    2,
    1,
    list_second_header,
)
for i in range(len(list_first_table)):

    worksheet.write_row(
        4 + i,
        1,
        list_first_table[i],
        mergeFormat(0, "left", "vcenter", "black", 12),
    )

worksheet.autofit()
workbook.close()
