class MockNode: pass # pragma: no cover
class MockEdge: pass # pragma: no cover
class MockDestination: pass # pragma: no cover
class MockFunction: pass # pragma: no cover
class Mock: pass # pragma: no cover
self = type('MockSelf', (object,), { 'converted_self': lambda self: MockNode(), '_node': MockNode(), '_function': MockFunction(), 'outgoing_edges': [] })() # pragma: no cover
_Node = MockNode # pragma: no cover

class MockGraphNode:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.name = ''# pragma: no cover
        self.op = ''# pragma: no cover
        self.input = []# pragma: no cover
        self.attr = {}# pragma: no cover
# pragma: no cover
    def Clear(self):# pragma: no cover
        self.name = ''# pragma: no cover
        self.op = ''# pragma: no cover
        self.input = []# pragma: no cover
        self.attr = {} # pragma: no cover
class MockNode:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.node = MockGraphNode()# pragma: no cover
        self.attr = {}# pragma: no cover
# pragma: no cover
    def Clear(self):# pragma: no cover
        self.node.Clear() # pragma: no cover
class MockEdge:# pragma: no cover
    def __init__(self, dest):# pragma: no cover
        self.destination = dest # pragma: no cover
class MockFunction:# pragma: no cover
    pass # pragma: no cover
class MockDestination:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.index = 0# pragma: no cover
        self.convertible = self# pragma: no cover
    def converted_self(self):# pragma: no cover
        return self # pragma: no cover
class MockSelf:# pragma: no cover
    def __init__(self):# pragma: no cover
        self._node = MockNode()# pragma: no cover
        self._function = MockFunction()# pragma: no cover
        # Creating multiple outgoing edges# pragma: no cover
        self.outgoing_edges = [MockEdge(MockDestination()) for _ in range(3)]# pragma: no cover
    def converted_self(self):# pragma: no cover
        return self # pragma: no cover
self = MockSelf() # pragma: no cover
_Node = MockNode # pragma: no cover

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
