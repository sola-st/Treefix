from collections import defaultdict # pragma: no cover

_Node = type('Node', (object,), {'node': type('InnerNode', (object,), {'input': ['value:input']})()})() # pragma: no cover

from collections import namedtuple # pragma: no cover
from collections import defaultdict # pragma: no cover

Node = namedtuple('Node', ['name', 'op', 'input', 'attr', 'Clear']) # pragma: no cover
Edge = namedtuple('Edge', ['destination']) # pragma: no cover
Destination = namedtuple('Destination', ['index', 'convertible']) # pragma: no cover
Convertible = namedtuple('Convertible', ['converted_self']) # pragma: no cover
NodeStruct = namedtuple('NodeStruct', ['node']) # pragma: no cover
destination_node = NodeStruct(node=Node(name='destination_node', op='ReadVariableOp', input=['destination_input:value'], attr={}, Clear=lambda: None)) # pragma: no cover
self = type('SelfMock', (object,), {})() # pragma: no cover
self._node = Node(name='node_name', op='ReadVariableOp', input=['input_node'], attr=defaultdict(lambda: tf.AttrValue(type=tf.dtypes.DType(tf.float32))), Clear=lambda: None) # pragma: no cover
self._function = True # pragma: no cover
self.outgoing_edges = [Edge(destination=Destination(index=0, convertible=Convertible(converted_self=lambda: destination_node)))] # pragma: no cover
self.converted_self = lambda: type('ConvertedSelfMock', (object,), {'node': Node(name='converted_node', op='Identity', input=[], attr=defaultdict(lambda: tf.AttrValue()), Clear=lambda: None)})() # pragma: no cover
_Node = type('NodeClassMock', (object,), {'node': Node(name='inner_node', op='Identity', input=['input_tensor:value'], attr=defaultdict(lambda: tf.AttrValue()), Clear=lambda: None)})() # pragma: no cover

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
