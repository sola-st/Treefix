# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/attention_ops_test.py
img = np.arange(9).reshape([1, 3, 3, 1])
with self.test_session():
    with self.assertRaises((errors.InvalidArgumentError, ValueError)):
        result = image_ops.extract_glimpse_v2(
            img,
            size=[1023, -63],
            offsets=[1023, 63],
            centered=False,
            normalized=False)
        self.evaluate(result)
