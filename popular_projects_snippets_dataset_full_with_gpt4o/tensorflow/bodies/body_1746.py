# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/pooling_ops_test.py
expected_output = [13.0, 14.0, 15.0, 16.0, 17.0, 18.0]
self._VerifyValues(nn_ops.max_pool,
                   input_sizes=[1, 2, 3, 3],
                   ksize=[1, 2, 2, 1],
                   strides=[1, 2, 2, 1],
                   padding="SAME",
                   expected=expected_output)
