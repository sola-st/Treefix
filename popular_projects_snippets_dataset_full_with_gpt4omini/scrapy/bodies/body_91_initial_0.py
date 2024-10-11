from typing import List, Any # pragma: no cover

nodes = ['node1', 'node2', 'node3'] # pragma: no cover
def iterate_spider_output(output: Any) -> List[Any]: return [output] # pragma: no cover

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
    _l_(6809)

    ret = iterate_spider_output(self.parse_node(response, selector))
    _l_(6806)
    for result_item in self.process_results(response, ret):
        _l_(6808)

        aux = result_item
        _l_(6807)
        exit(aux)
