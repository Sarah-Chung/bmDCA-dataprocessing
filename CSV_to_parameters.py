import numpy as np
import csv
import bmDCA_to_CSV as bm

# CHANGE ###########################################
numSites = 21
seqLen = 70 # change per domain
input_file = 'bmDCA_output_PF16725.txt' # bmDCA output

output_h = 'parameters_h_PF16725.csv' # bmDCA to CSV
output_e = 'parameters_e_PF16725.csv' # bmDCA to CSV

final_h = 'final_h_PF16725.csv' # formatted parameters
final_e = 'final_e_PF16725.csv' # formatted parameters
####################################################

if __name__ == "__main__":
    input_h = bm.h_csv(input_file,output_h,seqLen)
    print("Converted bmDCA to CSV -h")
    input_e = bm.e_csv(input_file, output_e,seqLen)
    print("Converted bmDCA to CSV -e")

def h_matrix(input_file, output_file,numSites):
    finalArr=[]

    # structuring h matrix data
    for i in range(numSites):
        with open(input_file,'r',newline='') as f:
            csv_reader = csv.reader(f,delimiter=',')
            seq = []
            for row in csv_reader:
                if int(row[2]) == i:
                    seq.append(row[3])
        finalArr.append(seq)

    # writing to output
    with open(output_file, 'w',newline='') as of:
        csv_writer = csv.writer(of)
        for line in finalArr:
            csv_writer.writerow(line)
    print("-h parameters completed.")
            
h_matrix(output_h,final_h,numSites)

def e_matrix(input_file,output_file,seqLen,numSites):
    finalArr = []
    c = np.array(finalArr)

    # For rows
    for i in range(seqLen): #(seqLen-2):
        arrays_list = []
        totalArr = np.array([])
        print("Array: " + str(i))

        zerosArr = np.zeros((21,21*(i+1)))
        final = np.array(zerosArr)

        # For columns
        for j in range(seqLen-1): #range(seqLen-(i+1)):
            sub = []
            with open(input_file, 'r', newline = '') as f:
                subArr = []
                csv_reader = csv.reader(f, delimiter = ',')

                for row in csv_reader:
                    if (int(row[1]) == i) and (int(row[2]) == j+(i+1)):
                        subArr.append(row[5])
                
                a = np.array(subArr)
                if a.size > 0:
                    data = a.reshape(21,21)
                else:
                    break
                #print(data)
                final = np.hstack((final, data))

        finalArr.append(final)
    
    # writing to output_file
    print(finalArr)
    with open(output_file, 'w', newline = '') as of:
        print("Writing to output file...")
        csv_writer = csv.writer(of)
        for row in finalArr:
            for value in row:
                csv_writer.writerow(value)
    
    print("-e parameters completed.")
            

e_matrix(output_e,final_e,111,21)