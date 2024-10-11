# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
with self.cached_session():
    with self.assertRaises(ValueError):
        l = array_ops.ones([int(2**11+1)], dtype=np.float16)
        du.get_logits_and_probs(
            logits=l, multidimensional=True, validate_args=True)

    with self.assertRaisesOpError(
        "Number of classes exceeds `dtype` precision"):
        l = array_ops.placeholder(dtype=dtypes.float16)
        logit, _ = du.get_logits_and_probs(
            logits=l, multidimensional=True, validate_args=True)
        logit.eval(feed_dict={l: np.ones([int(2**11+1)])})
