import xlsxwriter

from ToCSV import (
    list_first_header,
    dict_second_header_new,
    list_first_table,
    list_third_header,
    )

list_second_header = [item for item in dict_second_header_new.values()]

workbook = xlsxwriter.Workbook("Glick2.xlsx")
worksheet = workbook.add_worksheet("Гликемический индекс")
worksheet.set_column("B:D", 9)
worksheet.set_row(1, 120)
worksheet.set_column(1, 300)

merge_format = workbook.add_format(
    {
        "bold": 1,
        "align": "center",
        "valign": "vcenter",
        "color": "red",
    }
)
merge_format.set_font_size(24)

merge_format2 = workbook.add_format(
    {
        "bold": 1,
        "align": "center",
        "valign": "vcenter",
    }
)
merge_format2.set_font_size(20)
merge_format2.set_text_wrap(True)
merge_format2.set_color("blue")
merge_format2.set_align("center")

worksheet.merge_range("B2:D2", list_first_header[0], merge_format)
merge_format3 = workbook.add_format(
    {
        "bold": 1,
        "align": "center",
        "valign": "vcenter",
        "color": "green",
        "font_size": 14,
    }
)

worksheet.merge_range(
    3,
    1,
    3,
    3,
    list_third_header[0],
    merge_format3,
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
    )

worksheet.autofit()
workbook.close()
