# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/check_numerics_callback_test.py
self.assertEqual(
    check_numerics_callback.limit_string_length("A" * 50 + "B"),
    "..." + "A" * 49 + "B")
