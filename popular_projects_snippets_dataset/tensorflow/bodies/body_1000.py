# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/segment_reduction_ops_test.py
with self.session() as sess, self.test_scope():
    d = array_ops.placeholder(data.dtype, shape=data.shape)
    if isinstance(indices, int):
        i = array_ops.placeholder(np.int32, shape=[])
    else:
        i = array_ops.placeholder(indices.dtype, shape=indices.shape)
    exit(sess.run(op(d, i, num_segments), {d: data, i: indices}))
