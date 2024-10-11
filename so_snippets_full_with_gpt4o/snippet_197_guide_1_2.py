import locale # pragma: no cover

try: locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252') # pragma: no cover
except locale.Error: locale.setlocale(locale.LC_ALL, '') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1823058/how-to-print-a-number-using-commas-as-thousands-separators
from l3.Runtime import _l_
try:
    import locale
    _l_(13624)

except ImportError:
    pass

locale.setlocale( locale.LC_ALL, '' )
_l_(13625)
locale.currency( 1234567.89, grouping = True )
_l_(13626)

'Portuguese_Brazil.1252'
_l_(13627)
'R$ 1.234.567,89'
_l_(13628)

