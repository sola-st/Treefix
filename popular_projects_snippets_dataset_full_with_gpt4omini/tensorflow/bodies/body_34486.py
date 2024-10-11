# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
with ops.Graph().as_default():
    q = data_flow_ops.FIFOQueue(
        5, (dtypes_lib.int32, dtypes_lib.float32),
        names=("i", "j"),
        shared_name="foo",
        name="Q")
self.assertTrue(isinstance(q.queue_ref, ops.Tensor))
self.assertProtoEquals("""
      name:'Q' device: "/device:CPU:*" op:'FIFOQueueV2'
      attr { key: 'component_types' value { list {
        type: DT_INT32 type : DT_FLOAT
      } } }
      attr { key: 'shapes' value { list {} } }
      attr { key: 'capacity' value { i: 5 } }
      attr { key: 'container' value { s: '' } }
      attr { key: 'shared_name' value { s: 'foo' } }
      """, q.queue_ref.op.node_def)
self.assertEqual(["i", "j"], q.names)
