# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/pool.py
make_pool_tests(
    tf.nn.avg_pool2d, allow_fully_quantize=True)(
        options, expected_tf_failures=160)
