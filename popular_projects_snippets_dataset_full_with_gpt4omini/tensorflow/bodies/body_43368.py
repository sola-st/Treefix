# Extracted from ./data/repos/tensorflow/tensorflow/python/util/protobuf/compare_test.py
pb = compare_test_pb2.Large()
pb.int64s.extend([1, 400, 999999999999999])
compare.NormalizeNumberFields(pb)
self.assertTrue(isinstance(pb.int64s[0], six.integer_types))
self.assertTrue(isinstance(pb.int64s[1], six.integer_types))
self.assertTrue(isinstance(pb.int64s[2], six.integer_types))
