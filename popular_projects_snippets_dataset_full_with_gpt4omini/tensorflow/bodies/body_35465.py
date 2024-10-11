# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/multinomial_op_test.py
classes = 5
with test_util.use_gpu():
    for batch in 0, 3:
        for samples in 0, 7:
            x = self.evaluate(
                random_ops.multinomial(
                    array_ops.zeros([batch, classes]), samples))
            self.assertEqual(x.shape, (batch, samples))
