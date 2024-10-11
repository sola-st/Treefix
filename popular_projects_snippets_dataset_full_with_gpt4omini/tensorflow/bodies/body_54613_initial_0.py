class MockGraph: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.edges = [] # pragma: no cover
enclosing_graph = MockGraph() # pragma: no cover
self = type('Mock', (object,), {'_enclosing_graph': None, '_outgoing_edges': [], '_converted_self': None})() # pragma: no cover
self._enclosing_graph = enclosing_graph # pragma: no cover
self._outgoing_edges = [] # pragma: no cover
self._converted_self = None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
from l3.Runtime import _l_
self._enclosing_graph = enclosing_graph
_l_(9255)
self._outgoing_edges = []
_l_(9256)
self._converted_self = None
_l_(9257)
