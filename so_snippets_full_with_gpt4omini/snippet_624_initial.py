# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/8142364/how-to-compare-two-dates
from l3.Runtime import _l_
try:
    import datetime
    _l_(2541)

except ImportError:
    pass

eight_am = datetime.time( 8,0,0 ) # Time, without a date
_l_(2542) # Time, without a date

datetime.datetime.now().time() > eight_am  
_l_(2543)  

