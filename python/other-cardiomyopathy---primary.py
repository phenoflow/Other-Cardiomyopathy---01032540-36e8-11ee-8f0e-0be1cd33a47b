# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"G343.00","system":"readv2"},{"code":"G550.00","system":"readv2"},{"code":"G552.00","system":"readv2"},{"code":"G554100","system":"readv2"},{"code":"G554500","system":"readv2"},{"code":"G554511","system":"readv2"},{"code":"G558000","system":"readv2"},{"code":"G558z00","system":"readv2"},{"code":"G559.00","system":"readv2"},{"code":"G55A.11","system":"readv2"},{"code":"G55y.00","system":"readv2"},{"code":"G55y000","system":"readv2"},{"code":"G55z.00","system":"readv2"},{"code":"Gyu5N00","system":"readv2"},{"code":"100966.0","system":"med"},{"code":"101015.0","system":"med"},{"code":"102955.0","system":"med"},{"code":"104529.0","system":"med"},{"code":"104658.0","system":"med"},{"code":"105398.0","system":"med"},{"code":"105651.0","system":"med"},{"code":"105798.0","system":"med"},{"code":"15990.0","system":"med"},{"code":"20035.0","system":"med"},{"code":"21852.0","system":"med"},{"code":"22993.0","system":"med"},{"code":"27683.0","system":"med"},{"code":"30667.0","system":"med"},{"code":"3204.0","system":"med"},{"code":"40834.0","system":"med"},{"code":"41488.0","system":"med"},{"code":"42043.0","system":"med"},{"code":"44272.0","system":"med"},{"code":"49844.0","system":"med"},{"code":"55850.0","system":"med"},{"code":"56635.0","system":"med"},{"code":"57306.0","system":"med"},{"code":"58938.0","system":"med"},{"code":"64673.0","system":"med"},{"code":"64837.0","system":"med"},{"code":"68685.0","system":"med"},{"code":"70855.0","system":"med"},{"code":"7320.0","system":"med"},{"code":"92266.0","system":"med"},{"code":"97617.0","system":"med"},{"code":"97780.0","system":"med"},{"code":"98020.0","system":"med"},{"code":"98634.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('other-cardiomyopathy-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["other-cardiomyopathy---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["other-cardiomyopathy---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["other-cardiomyopathy---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
