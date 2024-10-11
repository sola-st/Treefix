from scrapy import Selector # pragma: no cover
from scrapy.http import Response # pragma: no cover

nodes = [Selector(text='<html><body></body></html>')] # pragma: no cover
iterate_spider_output = lambda x: [x] # pragma: no cover
response = Response('http://example.com') # pragma: no cover
self = type('Mock', (object,), { 'parse_node': lambda self, response, selector: {}, 'process_results': lambda self, response, ret: [{'item': 'example'}] })() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spiders/feed.py
from l3.Runtime import _l_
"""This method is called for the nodes matching the provided tag name
        (itertag). Receives the response and an Selector for each node.
        Overriding this method is mandatory. Otherwise, you spider won't work.
        This method must return either an item, a request, or a list
        containing any of them.
        """

for selector in nodes:
    _l_(17567)

    ret = iterate_spider_output(self.parse_node(response, selector))
    _l_(17564)
    for result_item in self.process_results(response, ret):
        _l_(17566)

        aux = result_item
        _l_(17565)
        exit(aux)
