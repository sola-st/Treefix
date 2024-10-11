class MockTensor: pass # pragma: no cover
class MockNodeDef: pass # pragma: no cover
class MockOp: pass # pragma: no cover
class MockQueueRef: pass # pragma: no cover
class MockTensorShape: pass # pragma: no cover
class MockGraph: pass # pragma: no cover
class MockFIFOQueue: pass # pragma: no cover
class MockDataFlowOps: pass # pragma: no cover
class MockDtypesLib: pass # pragma: no cover
class MockTensorShape: pass # pragma: no cover
class MockSelf: pass # pragma: no cover
 # pragma: no cover
ops = type('Mock', (object,), {'Graph': MockGraph, 'Tensor': MockTensor})() # pragma: no cover
data_flow_ops = type('Mock', (object,), {'FIFOQueue': MockFIFOQueue})() # pragma: no cover
dtypes_lib = type('Mock', (object,), {'int32': 'DT_INT32', 'float32': 'DT_FLOAT'})() # pragma: no cover
tensor_shape = type('Mock', (object,), {'TensorShape': MockTensorShape})() # pragma: no cover
self = MockSelf() # pragma: no cover

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
