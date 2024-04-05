import argparse
import xlsxwriter

def get_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=True, help="This is input file.")
    parser.add_argument("-x", "--output", required=True, help="This is output file.")
#    parser.add_argument("p", "--profrssion", default="all", choices = ['boxer', 'baker', 'programmer', 'all'], help="This is output format")
    
    args = parser.parse_args()
    fname = args.file
    output = args.output
    return fname, output

def get_content(fname):
    with open(fname) as f:
        return f.readlines()

def people_dict(ml):
    tmp = {}
    tmp["name"] = ml[0]
    tmp["surname"] = ml[1]
    tmp["age"] = int(ml[2])
    tmp["profession"] = ml[3]
    tmp["country"] = ml[4]
    return tmp

def people_list(content):
    header = content[0].strip().split()
    peoples = [header]
    for line in content[1:]:
        person = line.strip().split()
        peoples.append(people_dict(person))
    return peoples


def create_workbook(output):
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
    bold_green = workbook.add_format({'bold': True, 'bg_color': 'green'})
    color = workbook.add_format()
    color.set_bg_color("green")

    return workbook, worksheet, bold_green, color

def fill_data(workbook, worksheet, bold_green, color, data):
    row = 0
    for line in data:
        col = 0
        if row == 0:
            for data_item in line:
                worksheet.write(row, col, data_item, bold_green)
                col += 1
        else:
            for data_item in line.values():
                worksheet.write(row, col, data_item, color)
                col += 1
        row += 1

    workbook.close()

def main(): 
    fname, output = get_argument()
    cnt = get_content(fname)
    peoples = people_list(cnt)
    workbook, worksheet, bold_green, color = create_workbook(output)
    fill_data(workbook, worksheet, bold_green, color,peoples)

    

if __name__ == "__main__":
    main()

