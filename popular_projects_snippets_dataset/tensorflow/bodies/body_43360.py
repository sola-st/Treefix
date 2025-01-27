# Extracted from ./data/repos/tensorflow/tensorflow/python/util/protobuf/compare_test.py
googletest.TestCase.assertEqual(self, True, compare.ProtoEq('a', 'a'))
googletest.TestCase.assertEqual(self, False, compare.ProtoEq('b', 'a'))
