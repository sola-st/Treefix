# Extracted from ./data/repos/tensorflow/tensorflow/python/util/protobuf/compare_test.py
"""Checks that all possible asserts fail with the given message."""
message = re.escape(textwrap.dedent(message))
self.assertRaisesRegex(AssertionError, message, self.assertProtoEqual, a, b,
                       **kwargs)
