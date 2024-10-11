from unittest.mock import Mock # pragma: no cover
import collections # pragma: no cover

self = Mock() # pragma: no cover
_Node = Mock() # pragma: no cover
self._node = Mock() # pragma: no cover
self._node.name = 'node_name' # pragma: no cover
self._node.input = ['input_tensor'] # pragma: no cover
self._node.attr = {'dtype': Mock(), '_class': Mock()} # pragma: no cover
self._function = Mock() # pragma: no cover
self.outgoing_edges = [Mock(destination=Mock(index=0, convertible=Mock(converted_self=Mock(node=Mock(input=['read_variable:value'])))))] # pragma: no cover

from collections import defaultdict # pragma: no cover

self = type('MockSelf', (object,), {})() # pragma: no cover
node = type('MockNode', (object,), {'Clear': lambda self: None, 'input': [], 'attr': defaultdict(lambda: type('MockAttr', (object,), {'CopyFrom': lambda self, other: None})())})() # pragma: no cover
self.converted_self = lambda: type('MockConvertedSelf', (object,), {'node': node})() # pragma: no cover
self._node = type('MockOriginalNode', (object,), {'name': 'original_node', 'input': ['input_0'], 'attr': {'dtype': type('MockAttr', (object,), {'CopyFrom': lambda self, other: None})(), '_class': type('MockAttr', (object,), {'CopyFrom': lambda self, other: None})()}})() # pragma: no cover
self._function = True # pragma: no cover
self.outgoing_edges = [type('MockEdge', (object,), {'destination': type('MockDestination', (object,), {'index': 0, 'convertible': type('MockConvertible', (object,), {'converted_self': lambda: type('MockConvertedSelf', (object,), {'node': type('MockDestNode', (object,), {'input': ['input_0:value']})()})()})()})()})()] # pragma: no cover
_Node = type('MockNodeClass', (object,), {}) # pragma: no cover

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
