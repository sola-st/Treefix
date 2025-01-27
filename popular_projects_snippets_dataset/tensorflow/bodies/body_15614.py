# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_to_sparse_op_test.py
rt = ragged_factory_ops.constant([['a', 'b'], ['c', 'd', 'e'], ['f'], [],
                                  ['g']])
st = self.evaluate(rt.to_sparse())
self.assertAllEqual(
    st.indices, [[0, 0], [0, 1], [1, 0], [1, 1], [1, 2], [2, 0], [4, 0]])
self.assertAllEqual(st.values, b'a b c d e f g'.split())
self.assertAllEqual(st.dense_shape, [5, 3])
