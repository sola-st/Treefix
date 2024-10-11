# Extracted from ./data/repos/tensorflow/tensorflow/python/util/protobuf/compare_test.py
self.assertAll('int64s: 0 int64s: 1')

self.assertSameNotEqual('int64s: 0 int64s: 1', 'int64s: 1 int64s: 0')
self.assertSameNotEqual('int64s: 0 int64s: 1 int64s: 2',
                        'int64s: 2 int64s: 1 int64s: 0')

self.assertSameNotEqual('int64s: 0', 'int64s: 0 int64s: 0')
self.assertSameNotEqual('int64s: 0 int64s: 1',
                        'int64s: 1 int64s: 0 int64s: 1')

self.assertNone('int64s: 0', 'int64s: 0 int64s: 2', """
                      int64s: 0
                    + int64s: 2
                    """)
self.assertNone('int64s: 0 int64s: 1', 'int64s: 0 int64s: 2', """
                      int64s: 0
                    - int64s: 1
                    ?         ^
                    + int64s: 2
                    ?         ^
                    """)
