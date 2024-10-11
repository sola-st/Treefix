# Extracted from ./data/repos/tensorflow/tensorflow/python/util/protobuf/compare_test.py
pb1 = compare_test_pb2.Large()
pb1.double_ = 1.2314352351231
pb2 = compare_test_pb2.Large()
pb2.double_ = 1.2314352
self.assertNotEqual(pb1.double_, pb2.double_)
compare.NormalizeNumberFields(pb1)
compare.NormalizeNumberFields(pb2)
self.assertEqual(pb1.double_, pb2.double_)
