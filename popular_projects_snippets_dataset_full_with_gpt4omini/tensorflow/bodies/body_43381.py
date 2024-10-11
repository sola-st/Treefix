# Extracted from ./data/repos/tensorflow/tensorflow/python/util/protobuf/compare_test.py
# Proto size should be larger than 2**16.
number_of_entries = 2**13
string_value = 'dummystr'  # Has length of 2**3.
pb1_txt = 'strings: "dummystr"\n' * number_of_entries
pb2 = compare_test_pb2.Small(strings=[string_value] * number_of_entries)
compare.assertProtoEqual(self, pb1_txt, pb2)

with self.assertRaises(AssertionError):
    compare.assertProtoEqual(self, pb1_txt + 'strings: "Should fail."', pb2)
