# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/check_numerics_callback_test.py
self.assertEqual(
    check_numerics_callback.limit_string_length("", max_len=2), "")
self.assertEqual(
    check_numerics_callback.limit_string_length("e", max_len=2), "e")
self.assertEqual(
    check_numerics_callback.limit_string_length("de", max_len=2), "de")
self.assertEqual(
    check_numerics_callback.limit_string_length("abcde", max_len=2),
    "...de")
