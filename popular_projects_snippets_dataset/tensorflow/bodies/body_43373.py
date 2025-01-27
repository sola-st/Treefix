# Extracted from ./data/repos/tensorflow/tensorflow/python/util/protobuf/compare_test.py
if isinstance(a, six.string_types) and isinstance(b, six.string_types):
    a, b = LargePbs(a, b)
compare.assertProtoEqual(self, a, b, **kwargs)
