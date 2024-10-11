from typing import List, Optional, Dict # pragma: no cover
class MockNode: pass # pragma: no cover
class MockEdge: pass # pragma: no cover
class MockFunction: pass # pragma: no cover
class MockConvertible: pass # pragma: no cover
class Mock: pass # pragma: no cover

class _Node:  # Mock implementation# pragma: no cover
    def __init__(self, name, dtype, class_attr=None):# pragma: no cover
        self.name = name# pragma: no cover
        self.attr = {'dtype': dtype}# pragma: no cover
        if class_attr is not None:# pragma: no cover
            self.attr['_class'] = class_attr# pragma: no cover
        self.input = ['input_tensor']# pragma: no cover
 # pragma: no cover
class MockEdge:# pragma: no cover
    def __init__(self, destination):# pragma: no cover
        self.destination = destination# pragma: no cover
 # pragma: no cover
mock_attr = {"dtype": "float32", "_class": ["class_name"]}# pragma: no cover
 # pragma: no cover
class MockConvertible:# pragma: no cover
    def converted_self(self):# pragma: no cover
        return MockNode()# pragma: no cover
 # pragma: no cover
class MockFunction:  # Mock to represent the context of a function# pragma: no cover
    pass# pragma: no cover
 # pragma: no cover
class MockNode:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.node = type('MockNodeInstance', (object,), {'Clear': lambda: None, 'name': '', 'op': '', 'input': [], 'attr': {}})()  # Create a mock node class with necessary attributes. # pragma: no cover

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
