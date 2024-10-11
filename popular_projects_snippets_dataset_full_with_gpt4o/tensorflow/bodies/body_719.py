# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/searchsorted_op_test.py
# Test against NumPy implementation (which is 1D only).
np.random.seed(1)
for side in ['left', 'right']:
    for dtype in [np.float32, np.int32]:
        values = np.random.uniform(
            low=-1000, high=1000, size=(10,)).astype(dtype)
        unsorted = np.random.uniform(
            low=-1000, high=1000, size=(20,)).astype(dtype)

        sorted_sequence = np.sort(unsorted)
        np_ans = np.searchsorted(sorted_sequence, values, side=side)

        with self.session() as session:
            with self.test_scope():
                tf_ans = array_ops.searchsorted(sorted_sequence, values, side=side)
            tf_out = session.run(tf_ans)
            self.assertAllEqual(np_ans, tf_out)
