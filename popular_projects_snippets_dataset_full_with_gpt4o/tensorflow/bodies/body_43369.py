# Extracted from ./data/repos/tensorflow/tensorflow/python/util/protobuf/compare_test.py
pb1 = compare_test_pb2.Large()
pb1.float_ = 1.2314352351231
pb2 = compare_test_pb2.Large()
pb2.float_ = 1.231435
self.assertNotEqual(pb1.float_, pb2.float_)
compare.NormalizeNumberFields(pb1)
compare.NormalizeNumberFields(pb2)
self.assertEqual(pb1.float_, pb2.float_)
