# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = (
    "tf.count_nonzero(input_tensor=input, dtype=dtype, name=name, "
    "reduction_indices=axis, keep_dims=keepdims)\n"
    )
_, unused_report, unused_errors, new_text = self._upgrade(text)
expected_text = (
    "tf.math.count_nonzero(input=input, dtype=dtype, name=name, "
    "axis=axis, keepdims=keepdims)\n"
    )
self.assertEqual(new_text, expected_text)
