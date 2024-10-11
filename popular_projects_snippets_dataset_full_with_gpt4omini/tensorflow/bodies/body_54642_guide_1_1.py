from typing import List, Dict # pragma: no cover
class Node: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.input = [] # pragma: no cover
        self.attr = {'T': Mock(), '_class': Mock()} # pragma: no cover
        self.name = '' # pragma: no cover
        self.op = '' # pragma: no cover
    def Clear(self): pass # pragma: no cover
class Mock: # pragma: no cover
    def CopyFrom(self, other): pass # pragma: no cover
class Edge: # pragma: no cover
    def __init__(self, index, destination): # pragma: no cover
        self.index = index # pragma: no cover
        self.destination = destination # pragma: no cover
class Function: pass # pragma: no cover
class Convertible: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.node = Node() # pragma: no cover

self = type('MockSelf', (object,), {})() # pragma: no cover
self.converted_self = lambda: Convertible() # pragma: no cover
self._node = Node() # pragma: no cover
self._node.name = 'test_node' # pragma: no cover
self._node.input = ['input_tensor'] # pragma: no cover
self._node.attr['dtype'] = 'float32' # pragma: no cover
self._node.attr['_class'] = Mock() # pragma: no cover
self._function = Function() # pragma: no cover
self.outgoing_edges = [Edge(index=0, destination=Convertible())] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
from l3.Runtime import _l_
node = self.converted_self().node
_l_(8024)
node.Clear()
_l_(8025)
node.name = self._node.name
_l_(8026)
node.op = "Identity"
_l_(8027)

node.input.append(self._node.input[0])
_l_(8028)
node.attr["T"].CopyFrom(self._node.attr["dtype"])
_l_(8029)
if "_class" in self._node.attr:
    _l_(8031)

    node.attr["_class"].CopyFrom(self._node.attr["_class"])
    _l_(8030)

# If the ReadVariableOp is part of a function, then every node having the
# ReadVariableOp one as its input will refer to it using a ":value"
# syntax. We need to change that to ":output".
if self._function is not None:
    _l_(8040)

    for edge in self.outgoing_edges:
        _l_(8039)

        index = edge.destination.index
        _l_(8032)
        dest = edge.destination.convertible.converted_self()
        _l_(8033)
        if isinstance(dest, _Node):
            _l_(8038)

            input_name_parts = dest.node.input[index].split(":")
            _l_(8034)
            if len(input_name_parts) > 1 and input_name_parts[1] == "value":
                _l_(8037)

                input_name_parts[1] = "output"
                _l_(8035)
                dest.node.input[index] = ":".join(input_name_parts)
                _l_(8036)
