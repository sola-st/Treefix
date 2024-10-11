import io # pragma: no cover

outfile = io.StringIO('Test content') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/16573332/jsondecodeerror-expecting-value-line-1-column-1-char-0
from l3.Runtime import _l_
outfile.close()
_l_(13988)

