# Extracted from https://stackoverflow.com/questions/227459/how-to-get-the-ascii-value-of-a-character
for ch in mystr:
    code = ord(ch)

for code in map(ord, mystr):

for code in mystr.encode('ascii'):

# If mystr is definitely str, not unicode
for code in bytearray(mystr):

# If mystr could be either str or unicode
for code in bytearray(mystr, 'ascii'):

