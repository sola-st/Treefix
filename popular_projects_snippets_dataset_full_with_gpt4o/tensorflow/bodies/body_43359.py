# Extracted from ./data/repos/tensorflow/tensorflow/python/util/protobuf/compare_test.py
"""Asserts that ProtoEq says a == b."""
a, b = LargePbs(a, b)
googletest.TestCase.assertEqual(self, compare.ProtoEq(a, b), True)
