# this script turns BMDCA output to CSV files
import csv

def h_csv(input_file,output_file,seqLen):
    with open(input_file,'r') as f, open(output_file,'w',newline='') as output:
        csv_writer = csv.writer(output)
        for line in f:
            lines = line.strip().split(' ')
            for i in range(seqLen):
                if (int(lines[2]) == i) and (lines[0]=='h'):
                    csv_writer.writerow(lines)
    output.close()
    return output_file

def e_csv(input_file, output_file, seqLen):
    with open(input_file,'r') as f, open(output_file,'w',newline='') as output:
        csv_writer = csv.writer(output)
        for line in f:
            lines = line.strip().split(' ')  # assuming tab-delimited text
            for i in range(seqLen):
                if (float(lines[3])==i) and (lines[0]=='J'):
                    csv_writer.writerow(lines)
    output.close()
    return output_file

#h_csv(input,output_h,seqLen)
#e_csv(input,output_e,seqLen)