import csv

inputFile = 'PF16725_msa_numerical.txt'
outputFile = 'PF16725_msa_numerical_matrix.csv'

def numToMatrix(input, output):
    with open(input, 'r') as file, open(output, 'w', newline = '') as outputFile:
        csv_writer = csv.writer(outputFile)
        first_line = file.readline().strip()
        value = first_line.split()
        seqLen = value[2]
        next(file)
        for line in file:
            eachLine = line.split()
            print(eachLine)
            csv_writer.writerow(eachLine)
    outputFile.close()

    return outputFile

numToMatrix(inputFile, outputFile)