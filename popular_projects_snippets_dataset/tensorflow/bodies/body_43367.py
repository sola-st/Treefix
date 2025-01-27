# Extracted from ./data/repos/tensorflow/tensorflow/python/util/protobuf/compare_test.py
pb = compare_test_pb2.Large()
pb.int64_ = 4
compare.NormalizeNumberFields(pb)
self.assertTrue(isinstance(pb.int64_, six.integer_types))

pb.int64_ = 4
compare.NormalizeNumberFields(pb)
self.assertTrue(isinstance(pb.int64_, six.integer_types))

pb.int64_ = 9999999999999999
compare.NormalizeNumberFields(pb)
self.assertTrue(isinstance(pb.int64_, six.integer_types))
