from collections import namedtuple # pragma: no cover

_Node = type('MockNode', (object,), {'node': type('MockNodeInner', (object,), {'input': ['input_tensor'], 'Clear': lambda self: None, '__init__': lambda self: None})()})() # pragma: no cover

from google.protobuf import descriptor_pb2 # pragma: no cover

MockAttr = type('MockAttr', (object,), {'CopyFrom': lambda self, other: None}) # pragma: no cover
MockNode = type('MockNode', (object,), {'Clear': lambda self: None, 'attr': {'T': MockAttr(), '_class': MockAttr()}, 'input': [], 'name': '', 'op': 'Identity'}) # pragma: no cover
ConvertedNode = type('ConvertedNode', (object,), {'node': MockNode()}) # pragma: no cover
EdgeDestination = type('EdgeDestination', (object,), {'index': 0, 'convertible': type('Convertible', (object,), {'converted_self': lambda self: ConvertedNode()})()}) # pragma: no cover
MockEdge = type('MockEdge', (object,), {'destination': EdgeDestination()}) # pragma: no cover
self = type('MockSelf', (object,), { # pragma: no cover
    'converted_self': lambda self: ConvertedNode(), # pragma: no cover
    '_node': MockNode(), # pragma: no cover
    '_function': None, # pragma: no cover
    'outgoing_edges': [MockEdge()] # pragma: no cover
})() # pragma: no cover
_Node = ConvertedNode # pragma: no cover

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
