# Extracted from ./data/repos/tensorflow/tensorflow/python/util/protobuf/compare_test.py
pb1 = compare_test_pb2.Large()
pb1.int64_ = 4
pb2 = compare_test_pb2.Large()
pb2.int64_ = 4
compare.assertProtoEqual(self, pb1, pb2)
