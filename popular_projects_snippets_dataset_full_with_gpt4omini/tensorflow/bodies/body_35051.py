# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
with self.cached_session():
    with self.assertRaises(ValueError):
        p = array_ops.ones([int(2**11+1)], dtype=np.float16)
        du.get_logits_and_probs(
            probs=p, multidimensional=True, validate_args=True)

    with self.assertRaisesOpError(
        "Number of classes exceeds `dtype` precision"):
        p = array_ops.placeholder(dtype=dtypes.float16)
        _, prob = du.get_logits_and_probs(
            probs=p, multidimensional=True, validate_args=True)
        prob.eval(feed_dict={p: np.ones([int(2**11+1)])})
