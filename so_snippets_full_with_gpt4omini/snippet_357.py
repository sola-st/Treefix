# Extracted from https://stackoverflow.com/questions/6081008/dump-a-numpy-array-into-a-csv-file
    for x in np.nditer(a.T, order='C'): 
            file.write(str(x))
            file.write("\n")

    writer= csv.writer(file, delimiter=',')
    for x in np.nditer(a.T, order='C'): 
            row.append(str(x))
    writer.writerow(row)

