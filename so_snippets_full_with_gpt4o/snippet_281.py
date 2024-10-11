# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5214578/print-string-to-text-file
from l3.Runtime import _l_
try:
    import datetime
    _l_(13644)

except ImportError:
    pass

now = datetime.datetime.now()
_l_(13645)
price = 1200
_l_(13646)
currency = "INR"
_l_(13647)

with open("D:\\log.txt","a") as f:
    _l_(13649)

    f.write(f'Product sold at {currency} {price } on {str(now)}\n')
    _l_(13648)

