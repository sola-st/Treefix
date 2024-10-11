# Extracted from https://stackoverflow.com/questions/8009882/how-to-read-a-large-file-line-by-line
HP-Z820:/mnt/fastssd/fast_file_reader$ ls -l /mnt/fastssd/nzv/HIGGS.csv
-rw-rw-r-- 1 8035497980 Jan 24 16:00 /mnt/fastssd/nzv/HIGGS.csv

HP-Z820:/mnt/fastssd$ ls -l all_bin.csv
-rw-rw-r-- 1 40412077758 Feb  2 09:00 all_bin.csv

ga@ga-HP-Z820:/mnt/fastssd$ time python fastread.py --fileName="all_bin.csv" --numProcesses=32 --balanceFactor=2
2367496

real    0m8.920s
user    1m30.056s
sys 2m38.744s

In [1]: 40412077758. / 8.92
Out[1]: 4530501990.807175

HP-Z820:/mnt/fastssd$ time wc -l all_bin.csv
2367496 all_bin.csv

real    0m8.807s
user    0m1.168s
sys 0m7.636s


HP-Z820:/mnt/fastssd/fast_file_reader$ time python fastread.py --fileName="HIGGS.csv" --numProcesses=16 --balanceFactor=2
11000000

real    0m2.257s
user    0m12.088s
sys 0m20.512s

HP-Z820:/mnt/fastssd/fast_file_reader$ time wc -l HIGGS.csv
11000000 HIGGS.csv

real    0m1.820s
user    0m0.364s
sys 0m1.456s

HP-Z820:/mnt/fastssd/fast_file_reader$ time python fastread.py --fileName="HIGGS.csv" --numProcesses=16 --balanceFactor=2
11000000

real    0m2.256s
user    0m10.696s
sys 0m19.952s

HP-Z820:/mnt/fastssd/fast_file_reader$ time python fastread.py --fileName="HIGGS.csv" --numProcesses=1 --balanceFactor=1
11000000

real    0m17.380s
user    0m11.124s
sys 0m6.272s

HP-Z820:/mnt/fastssd/fast_file_reader$ time python fastread.py --fileName="HIGGS.csv" --numProcesses=1 --balanceFactor=2
11000000

real    1m37.077s
user    0m12.432s
sys 1m24.700s

fileBytes = stat(fileName).st_size  # Read quickly from OS how many bytes are in a text file
startByte, endByte = PartitionDataToWorkers(workers=numProcesses, items=fileBytes, balanceFactor=balanceFactor)
p = Pool(numProcesses)
partialSum = p.starmap(ReadFileSegment, zip(startByte, endByte, repeat(fileName))) # startByte is already a list. fileName is made into a same-length list of duplicates values.
globalSum = sum(partialSum)
print(globalSum)


def ReadFileSegment(startByte, endByte, fileName, searchChar='\n'):  # counts number of searchChar appearing in the byte range
    with open(fileName, 'r') as f:
        f.seek(startByte-1)  # seek is initially at byte 0 and then moves forward the specified amount, so seek(5) points at the 6th byte.
        bytes = f.read(endByte - startByte + 1)
        cnt = len(re.findall(searchChar, bytes)) # findall with implicit compiling runs just as fast here as re.compile once + re.finditer many times.
    return cnt

