# Extracted from ./data/repos/tensorflow/tensorflow/python/util/protobuf/compare_test.py
pb = compare_test_pb2.Large()
pb.string_ = 'abc'
pb.float_ = 1.234
compare.assertProtoEqual(self, """
          string_: 'abc'
          float_: 1.234
        """, pb)
