class MockSelf: # pragma: no cover
    def assertTrue(self, condition): # pragma: no cover
        assert condition # pragma: no cover
    def assertProtoEquals(self, expected, actual): # pragma: no cover
        expected_proto = node_def_pb2.NodeDef() # pragma: no cover
        text_format.Merge(expected, expected_proto) # pragma: no cover
        actual_str = str(actual).replace(' ', '').replace('\n', '') # pragma: no cover
        expected_proto_str = str(expected_proto).replace(' ', '').replace('\n', '') # pragma: no cover
        assert expected_proto_str in actual_str, f'Expected: {expected_proto_str}, but got: {actual_str}' # pragma: no cover
    def assertEqual(self, first, second): # pragma: no cover
        assert first == second # pragma: no cover
def _l_(line_number): pass # pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
from l3.Runtime import _l_
with ops.Graph().as_default():
    _l_(20750)

    q = data_flow_ops.FIFOQueue(
        5, (dtypes_lib.int32, dtypes_lib.float32),
        names=("i", "f"),
        shapes=(tensor_shape.TensorShape([1, 1, 2, 3]),
                tensor_shape.TensorShape([5, 8])),
        name="Q")
    _l_(20749)
self.assertTrue(isinstance(q.queue_ref, ops.Tensor))
_l_(20751)
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
_l_(20752)
self.assertEqual(["i", "f"], q.names)
_l_(20753)
