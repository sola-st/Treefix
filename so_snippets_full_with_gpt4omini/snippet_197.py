# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1823058/how-to-print-a-number-using-commas-as-thousands-separators
from l3.Runtime import _l_
try:
    import locale
    _l_(2224)

except ImportError:
    pass

locale.setlocale( locale.LC_ALL, '' )
_l_(2225)
locale.currency( 1234567.89, grouping = True )
_l_(2226)

'Portuguese_Brazil.1252'
_l_(2227)
'R$ 1.234.567,89'
_l_(2228)

