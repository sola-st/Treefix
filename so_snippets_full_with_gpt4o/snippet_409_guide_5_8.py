import csv # pragma: no cover
import sys # pragma: no cover
import os # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row
#!python3
from l3.Runtime import _l_
with open('/pythonwork/thefile_subset11.csv', 'w', newline='') as outfile:
    _l_(15007)

    writer = csv.writer(outfile)
    _l_(15006)

#!python2
with open('/pythonwork/thefile_subset11.csv', 'wb') as outfile:
    _l_(15009)

    writer = csv.writer(outfile)
    _l_(15008)

