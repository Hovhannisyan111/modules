import argparse
import xlsxwriter

def get_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=True, help="This is input file.")
    parser.add_argument("-x", "--output", required=True, help="This is output file.")
    parser.add_argument("-s", "--sheet", help="This is output format")
    
    args = parser.parse_args()
    fname = args.file
    output = args.output
    sheet = args.sheet
    return fname, output, sheet 

def get_content(fname):
    with open(fname) as f:
        return f.readlines()

def people_dict(n, s, a, p, add):
    tmp = {}
    tmp["name"] = n
    tmp["surname"] = s
    tmp["age"] = a
    tmp["profession"] = p
    tmp["address"] = add
    return tmp

def people_list(content):
    ml = []
    for line in content:
        name, surname, age, profession, address = line.split()
        ml.append(people_dict(name, surname, age, profession, address))
    return ml
    


def create_workbook(output):
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': True, 'bg_color': 'green'})
    color = workbook.add_format()
    color.set_bg_color("yellow")

    return workbook, worksheet, bold, color

def fill_data(workbook, worksheet, sheet,bold, color, data):
    
    worksheet.write(0, 0, "Name", bold)
    worksheet.write(0, 1, "Surname", bold)
    worksheet.write(0, 2, "Age", bold)
    worksheet.write(0, 3, "Profession", bold)
    worksheet.write(0, 4, "Address", bold)
    row = 1
    for i in data:
        worksheet.write(row, 0, i["name"])
        worksheet.write(row, 1, i["surname"])
        if int(i["age"]) > 35:
            worksheet.write(row, 2, i["age"], color)
        else:
            worksheet.write(row, 2, i["age"])
        worksheet.write(row, 3, i["profession"])
        worksheet.write(row, 4, i["address"])
        row += 1
    if sheet:
        row2 = 0
        worksheet2 = workbook.add_worksheet(sheet)
        for i in data:
            if i["profession"] == sheet:
                worksheet2.write(row2, 0, i["name"])
                worksheet2.write(row2, 1, i["surname"])
                worksheet2.write(row2, 2, i["age"])
                worksheet2.write(row2, 3, i["profession"])
                worksheet2.write(row2, 4, i["address"])
                row2 += 1

            if i["address"] == sheet:
                worksheet2.write(row2, 0, i["name"])
                worksheet2.write(row2, 1, i["surname"])
                worksheet2.write(row2, 2, i["age"])
                worksheet2.write(row2, 3, i["profession"])
                worksheet2.write(row2, 4, i["address"])
                row2 += 1

    workbook.close()

def main(): 
    fname, output, sheet = get_argument()
    cnt = get_content(fname)
    peoples = people_list(cnt)
    workbook, worksheet, bold, color = create_workbook(output)
    fill_data(workbook, worksheet, sheet,bold, color,peoples)
    

if __name__ == "__main__":
    main()

