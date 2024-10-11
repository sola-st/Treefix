# Extracted from ./data/repos/tensorflow/tensorflow/python/util/protobuf/compare_test.py
pb = compare_test_pb2.Large()
pb.medium.floats.extend([0.111111111, 0.111111])
compare.NormalizeNumberFields(pb)
for value in pb.medium.floats:
    self.assertAlmostEqual(0.111111, value)
