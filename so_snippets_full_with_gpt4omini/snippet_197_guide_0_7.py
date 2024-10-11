import locale # pragma: no cover

class Mock(object): pass # pragma: no cover
locale = Mock() # pragma: no cover
locale.setlocale = lambda category, locale_name: None # pragma: no cover
locale.currency = lambda amount, grouping: 'R$ 1.234.567,89' # pragma: no cover
locale.LC_ALL = 0 # pragma: no cover

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

