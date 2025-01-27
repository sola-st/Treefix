# Extracted from ./data/repos/tensorflow/tensorflow/python/util/protobuf/compare_test.py
self.assertRaisesRegex(
    AssertionError,
    'test message passed down',
    self.assertProtoEqual,
    'medium: {}',
    'medium: { smalls: { strings: "x" } }',
    msg='test message passed down')
