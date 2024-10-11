self = type('Mock', (object,), {})() # pragma: no cover
self.file = 'example_file.txt' # pragma: no cover
self.plugins = [lambda x, opts: x + '_plugin1', lambda x, opts: x + '_plugin2'] # pragma: no cover
self.feed_options = 'feed_options_example' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/postprocessing.py
from l3.Runtime import _l_
prev = self.file
_l_(18666)
for plugin in self.plugins[::-1]:
    _l_(18668)

    prev = plugin(prev, self.feed_options)
    _l_(18667)
aux = prev
_l_(18669)
exit(aux)
