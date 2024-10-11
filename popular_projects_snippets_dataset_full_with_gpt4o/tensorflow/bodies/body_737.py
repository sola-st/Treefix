# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/concat_ops_test.py
c1 = np.random.rand(4, 4).astype(np.float32)
c2 = np.random.rand(4, 4).astype(np.float32)
with self.session():
    with self.test_scope():
        concat_list_t = array_ops.concat([c1, c2], 0)
        concat_tuple_t = array_ops.concat((c1, c2), 0)
    self.assertAllEqual(concat_list_t, self.evaluate(concat_tuple_t))
