# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/44778/how-would-you-make-a-comma-separated-string-from-a-list-of-strings
from l3.Runtime import _l_
try:
    import csv
    _l_(13930)

except ImportError:
    pass
with open('some.csv', 'w', newline='') as f:
    _l_(13933)

    writer = csv.writer(f)
    _l_(13931)
    writer.writerow(l)  # this will output l as a single row.  
    _l_(13932)  # this will output l as a single row.  

