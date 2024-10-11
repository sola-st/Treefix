from typing import List, Callable # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.file = 'initial_data' # pragma: no cover
self.plugins = [lambda x, options: x + ' processed by plugin1', lambda x, options: x + ' processed by plugin2'] # pragma: no cover
self.feed_options = {'option1': 'value1', 'option2': 'value2'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/postprocessing.py
from l3.Runtime import _l_
prev = self.file
_l_(7820)
for plugin in self.plugins[::-1]:
    _l_(7822)

    prev = plugin(prev, self.feed_options)
    _l_(7821)
aux = prev
_l_(7823)
exit(aux)
