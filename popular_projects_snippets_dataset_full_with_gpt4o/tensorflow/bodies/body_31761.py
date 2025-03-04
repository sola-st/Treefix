# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_3d_test.py
# Test case for GitHub issue 51936.
for f in [nn_ops.max_pool3d, nn_ops.avg_pool3d]:
    with self.session():
        with self.assertRaises((errors.InvalidArgumentError, ValueError)):
            input_sizes = [3, 4, 10, 11, 12]

            input_data = 1.
            input_tensor = constant_op.constant(
                input_data, shape=input_sizes, name="input")
            pool_3d = f(input_tensor, ksize=[2, 2, 0], strides=1, padding="VALID")
            self.evaluate(pool_3d)
