# Extracted from https://stackoverflow.com/questions/1841565/valueerror-invalid-literal-for-int-with-base-10
\x00\x31\x00\x0d\x00

countStr = fields[3].replace('\x00', '').strip()
count = int(countStr)

