# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/check_numerics_callback_test.py
self.assertEqual(check_numerics_callback.limit_string_length(
    "A" * 100 + "B", max_len=None), "A" * 100 + "B")
self.assertEqual(
    check_numerics_callback.limit_string_length("", max_len=None), "")
