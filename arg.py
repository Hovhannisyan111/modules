import argparse
import os

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=True, help="Input file option.")
    parser.add_argument("-o", "--output",required=True, help="Output file option.")
    
    args = parser.parse_args()
    filename = args.file
    output = args.output
    return filename, output

def create(filename, output):
    created = []
    existed = []
    
    with open(output, 'w') as fw:
        with open(filename, 'r') as f:
            for i in f:
                dname = i.strip()
                if not os.path.exists(dname):
                    os.makedirs(dname)
                    created.append(dname)
                else: 
                    existed.append(dname)
        fw.write("Existed:\n")
        for dname in sorted(existed):
            fw.write(dname+"\n")
        fw.write("Created:\n")
        for dname in sorted(created):
            fw.write(dname+"\n")

def main():
    filename, output = get_arguments()
    create(filename, output)

if __name__ == "__main__":
    main()
