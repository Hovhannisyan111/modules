import xlsxwriter
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required=True, help="Input file option.")
    parser.add_argument('-o','--output', required=True, help="output option.")
    args = parser.parse_args()
    filename = args.file
    output = args.output
    return filename, output

def get_content(fname):
    with open(fname) as f:
        return f.readlines()

def create_excel(output_name, data):
    workbook = xlsxwriter.Workbook(output_name)
    worksheet = workbook.add_worksheet()

    row = 0
    for line in data:
        worksheet.write(row, 0, line.strip())
        row += 1
    workbook.close()

def main():
    filename, output = get_arguments()
    data = get_content(filename)
    create_excel(output, data)

if __name__ == "__main__":
    main()
