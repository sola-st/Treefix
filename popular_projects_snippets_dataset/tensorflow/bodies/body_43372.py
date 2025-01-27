# Extracted from ./data/repos/tensorflow/tensorflow/python/util/protobuf/compare_test.py
pb = compare_test_pb2.WithMap()
pb.value_message[4].strings.extend(['a', 'b', 'c'])
pb.value_string['d'] = 'e'
compare.NormalizeNumberFields(pb)
