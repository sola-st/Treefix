from __future__ import unicode_literals # pragma: no cover

u = 'idzie wąż wąską dróżką' # pragma: no cover
uu = u # pragma: no cover
s = uu.encode('cp1250') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6289474/working-with-utf-8-encoding-in-python-source
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from l3.Runtime import _l_
u = 'idzie wąż wąską dróżką'
_l_(1552)
uu = u.decode('utf8')
_l_(1553)
s = uu.encode('cp1250')
_l_(1554)
print(s)
_l_(1555)

