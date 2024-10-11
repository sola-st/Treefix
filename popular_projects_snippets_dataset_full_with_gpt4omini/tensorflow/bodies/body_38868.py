# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
with ops.Graph().as_default():
    q = data_flow_ops.SparseConditionalAccumulator(
        dtypes_lib.float32,
        name="Q",
        shape=tensor_shape.TensorShape([1, 5, 2, 8]))
self.assertTrue(isinstance(q.accumulator_ref, ops.Tensor))
self.assertProtoEquals(
    """
      name:'Q' op:'SparseConditionalAccumulator'
      attr { key: 'dtype' value { type: DT_FLOAT } }
      attr { key: 'shape' value { shape { dim {size: 1 }
                                          dim {size: 5 }
                                          dim {size: 2 }
                                          dim {size: 8 }
      } } }
      attr { key: 'container' value { s: '' } }
      attr { key: 'shared_name' value { s: '' } }
      attr { key: 'reduction_type' value {s: 'MEAN'} }
      """, q.accumulator_ref.op.node_def)
