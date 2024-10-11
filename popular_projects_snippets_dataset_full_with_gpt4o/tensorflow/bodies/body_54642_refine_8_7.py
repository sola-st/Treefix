from collections import defaultdict # pragma: no cover
import types # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
self.converted_self = lambda: self # pragma: no cover
self._node = type('MockNode', (object,), {'name': 'example_name', 'input': ['example_input'], 'attr': defaultdict(lambda: type('MockAttr', (object,), {'CopyFrom': lambda x: None})())})() # pragma: no cover
self._function = types.SimpleNamespace() # pragma: no cover
self.outgoing_edges = [type('MockEdge', (object,), {'destination': type('MockDestination', (object,), {'convertible': self, 'index': 0})()})()] # pragma: no cover
_Node = type('MockNodeClass', (object,), {}) # pragma: no cover

from collections import defaultdict # pragma: no cover
import types # pragma: no cover

class MockAttr: # pragma: no cover
    def CopyFrom(self, other): # pragma: no cover
        pass # pragma: no cover
class MockNode: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.name = 'example_name' # pragma: no cover
        self.op = '' # pragma: no cover
        self.input = ['example_input'] # pragma: no cover
        self.attr = defaultdict(MockAttr) # pragma: no cover
    def Clear(self): # pragma: no cover
        self.name = '' # pragma: no cover
        self.op = '' # pragma: no cover
        self.input = [] # pragma: no cover
        self.attr = defaultdict(MockAttr) # pragma: no cover
class MockFunction: # pragma: no cover
    pass # pragma: no cover
self = type('MockSelf', (object,), {'converted_self': lambda self: MockConvertedSelf(), '_node': MockNode(), '_function': MockFunction(), 'outgoing_edges': []})() # pragma: no cover
class MockConvertedSelf: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.node = MockNode() # pragma: no cover
_Node = type('MockNodeClass', (object,), {'node': MockNode()}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
from l3.Runtime import _l_
node = self.converted_self().node
_l_(20648)
node.Clear()
_l_(20649)
node.name = self._node.name
_l_(20650)
node.op = "Identity"
_l_(20651)

node.input.append(self._node.input[0])
_l_(20652)
node.attr["T"].CopyFrom(self._node.attr["dtype"])
_l_(20653)
if "_class" in self._node.attr:
    _l_(20655)

    node.attr["_class"].CopyFrom(self._node.attr["_class"])
    _l_(20654)

# If the ReadVariableOp is part of a function, then every node having the
# ReadVariableOp one as its input will refer to it using a ":value"
# syntax. We need to change that to ":output".
if self._function is not None:
    _l_(20664)

    for edge in self.outgoing_edges:
        _l_(20663)

        index = edge.destination.index
        _l_(20656)
        dest = edge.destination.convertible.converted_self()
        _l_(20657)
        if isinstance(dest, _Node):
            _l_(20662)

            input_name_parts = dest.node.input[index].split(":")
            _l_(20658)
            if len(input_name_parts) > 1 and input_name_parts[1] == "value":
                _l_(20661)

                input_name_parts[1] = "output"
                _l_(20659)
                dest.node.input[index] = ":".join(input_name_parts)
                _l_(20660)
