from collections import namedtuple # pragma: no cover
import types # pragma: no cover
import unittest.mock as mock # pragma: no cover

self = type('SelfMock', (object,), {})() # pragma: no cover
self.converted_self = mock.Mock(return_value=self) # pragma: no cover
Node = namedtuple('Node', ['name', 'op', 'input', 'attr']) # pragma: no cover
self._node = Node(name='node_name', op='op_type', input=['input_0'], attr={'dtype': mock.Mock(), '_class': mock.Mock()}) # pragma: no cover
self._function = mock.Mock() # pragma: no cover
Edge = namedtuple('Edge', ['destination']) # pragma: no cover
Destination = namedtuple('Destination', ['index', 'convertible']) # pragma: no cover
Convertible = namedtuple('Convertible', ['converted_self']) # pragma: no cover
NodeStruct = namedtuple('NodeStruct', ['node']) # pragma: no cover
dest_node = NodeStruct(node=Node(name='', op='', input=['input_0:value'], attr={})) # pragma: no cover
self.outgoing_edges = [Edge(destination=Destination(index=0, convertible=Convertible(converted_self=mock.Mock(return_value=dest_node))))] # pragma: no cover
_Node = type('NodeClassMock', (object,), {}) # pragma: no cover

from collections import defaultdict # pragma: no cover
from typing import List # pragma: no cover

self = type('Mock', (object,), {'converted_self': lambda self: self, 'node': type('NodeMock', (object,), {'Clear': lambda self: None, 'name': '', 'op': '', 'input': [], 'attr': defaultdict(lambda: type('MockAttr', (object,), {'CopyFrom': lambda x: None})())})()})() # pragma: no cover
_Node = type('_Node', (object,), {}) # pragma: no cover
self._node = type('MockNode', (object,), {'name': 'node_name', 'input': ['input_0'], 'attr': {'dtype': type('MockAttr', (object,), {'CopyFrom': lambda x: None})(), '_class': type('MockAttr', (object,), {'CopyFrom': lambda x: None})()}})() # pragma: no cover
self._function = None # pragma: no cover
self.outgoing_edges = [type('MockEdge', (object,), {'destination': type('MockDestination', (object,), {'index': 0, 'convertible': type('MockConvertible', (object,), {'converted_self': lambda: type('MockNodeDest', (object,), {'node': type('MockNodeDestInner', (object,), {'input': ['destination_input:value']})()})()})()})()})()] # pragma: no cover

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
