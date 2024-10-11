# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type_test.py

with self.assertLogs(level="WARNING") as logs:
    result = function_type.sanitize_arg_name("96ab.cd//?53")

self.assertEqual(result, "arg_96ab_cd___53")

expected_message = (
    "WARNING:absl:`96ab.cd//?53` is not a valid tf.function parameter name."
    " Sanitizing to `arg_96ab_cd___53`.")
self.assertIn(expected_message, logs.output)
