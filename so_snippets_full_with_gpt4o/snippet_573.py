# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/7999935/python-datetime-to-string-without-microsecond-component
from l3.Runtime import _l_
try:
    import datetime
    _l_(14815)

except ImportError:
    pass

date_generated = datetime.datetime.now()
_l_(14816)
date_generated.replace(microsecond=0).isoformat(' ').partition('+')[0]
_l_(14817)

