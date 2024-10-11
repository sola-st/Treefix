# Extracted from ./data/repos/tensorflow/tensorflow/python/util/protobuf/compare_test.py
pb1 = compare_test_pb2.Large()
pb1.double_ = 4.0
pb2 = compare_test_pb2.Large()
pb2.double_ = 4
compare.assertProtoEqual(self, pb1, pb2, normalize_numbers=True)
