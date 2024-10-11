# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/reverse_ops_test.py
np.random.seed(120)
pval = np.random.randint(0, 100, size=shape).astype(float)
with self.session():
    with self.test_scope():
        p = array_ops.placeholder(dtypes.int32, shape=shape)
        axis = constant_op.constant(
            np.array(revdims, dtype=np.int32),
            shape=(len(revdims),),
            dtype=dtypes.int32)
        rval = array_ops.reverse(p, axis).eval({p: pval})

        slices = tuple(
            slice(-1, None, -1)
            if d in revdims or d - len(shape) in revdims else slice(None)
            for d in range(len(shape))
        )
    self.assertEqual(pval[slices].flatten().tolist(), rval.flatten().tolist())
