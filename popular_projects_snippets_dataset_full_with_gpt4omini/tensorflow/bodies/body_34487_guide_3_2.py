class MockNodeDef: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.name = 'Q' # pragma: no cover
        self.device = '/device:CPU:*' # pragma: no cover
        self.op = 'FIFOQueueV2' # pragma: no cover
        self.attr = { # pragma: no cover
            'component_types': {'list': [{'type': dtypes_lib.int32}, {'type': dtypes_lib.float32}]}, # pragma: no cover
            'shapes': {'list': [{'shape': [{'dim': [{'size': 1}, {'size': 1}, {'size': 2}, {'size': 3}]}]}, {'shape': [{'dim': [{'size': 5}, {'size': 8}]}]}]}, # pragma: no cover
            'capacity': {'i': 5}, # pragma: no cover
            'container': {'s': ''}, # pragma: no cover
            'shared_name': {'s': ''} # pragma: no cover
        } # pragma: no cover
class MockOp: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.node_def = MockNodeDef() # pragma: no cover
class MockQueueRef: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.op = MockOp() # pragma: no cover
class MockFIFOQueue: # pragma: no cover
    def __init__(self, capacity, dtypes, names, shapes, name): # pragma: no cover
        self.queue_ref = MockQueueRef() # pragma: no cover
        self.names = names # pragma: no cover
self = type('MockSelf', (object,), {})() # pragma: no cover
self.assertTrue = lambda condition: print('Assert True:', condition) # pragma: no cover
self.assertProtoEquals = lambda proto, node_def: print('Proto comparison:', proto == node_def) # pragma: no cover
self.assertEqual = lambda a, b: print('Assert Equal:', a == b) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
from l3.Runtime import _l_
with ops.Graph().as_default():
    _l_(8094)

    q = data_flow_ops.FIFOQueue(
        5, (dtypes_lib.int32, dtypes_lib.float32),
        names=("i", "f"),
        shapes=(tensor_shape.TensorShape([1, 1, 2, 3]),
                tensor_shape.TensorShape([5, 8])),
        name="Q")
    _l_(8093)
self.assertTrue(isinstance(q.queue_ref, ops.Tensor))
_l_(8095)
self.assertProtoEquals("""
      name:'Q' device: "/device:CPU:*" op:'FIFOQueueV2'
      attr { key: 'component_types' value { list {
        type: DT_INT32 type : DT_FLOAT
      } } }
      attr { key: 'shapes' value { list {
        shape { dim { size: 1 }
                dim { size: 1 }
                dim { size: 2 }
                dim { size: 3 } }
        shape { dim { size: 5 }
                dim { size: 8 } }
      } } }
      attr { key: 'capacity' value { i: 5 } }
      attr { key: 'container' value { s: '' } }
      attr { key: 'shared_name' value { s: '' } }
      """, q.queue_ref.op.node_def)
_l_(8096)
self.assertEqual(["i", "f"], q.names)
_l_(8097)
