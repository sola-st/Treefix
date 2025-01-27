# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
with ops.Graph().as_default():
    q = data_flow_ops.SparseConditionalAccumulator(
        dtypes_lib.float32, name="Q")
self.assertTrue(isinstance(q.accumulator_ref, ops.Tensor))
self.assertProtoEquals(
    """
      name:'Q' op:'SparseConditionalAccumulator'
      attr { key: 'dtype' value { type: DT_FLOAT } }
      attr { key: 'shape' value { shape { unknown_rank: true} } }
      attr { key: 'container' value { s: '' } }
      attr { key: 'shared_name' value { s: '' } }
      attr { key: 'reduction_type' value {s: 'MEAN'} }
      """, q.accumulator_ref.op.node_def)
