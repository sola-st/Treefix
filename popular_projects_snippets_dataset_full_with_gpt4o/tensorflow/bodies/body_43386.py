# Extracted from ./data/repos/tensorflow/tensorflow/python/util/protobuf/compare_test.py
self.assertAll('medium: { smalls: {} smalls: {} }')
self.assertAll('medium: { smalls: { strings: "x" } } medium: {}')
self.assertAll('medium: { smalls: { strings: "x" } } medium: { int32s: 0 }')
self.assertAll('medium: { smalls: {} smalls: { strings: "x" } } small: {}')

self.assertSameNotEqual('medium: { smalls: { strings: "x" } smalls: {} }',
                        'medium: { smalls: {} smalls: { strings: "x" } }')

self.assertSameNotEqual('medium: { smalls: {} }',
                        'medium: { smalls: {} smalls: {} }')
self.assertSameNotEqual('medium: { smalls: {} smalls: {} } medium: {}',
                        'medium: {} medium: {} medium: { smalls: {} }')
self.assertSameNotEqual(
    'medium: { smalls: { strings: "x" } smalls: {} }',
    'medium: { smalls: {} smalls: { strings: "x" } smalls: {} }')

self.assertNone('medium: {}', 'medium: {} medium { smalls: {} }', """
                      medium {
                    +   smalls {
                    +   }
                      }
                    """)
self.assertNone('medium: { smalls: {} smalls: { strings: "x" } }',
                'medium: { smalls: {} smalls: { strings: "y" } }', """
                      medium {
                        smalls {
                        }
                        smalls {
                    -     strings: "x"
                    ?               ^
                    +     strings: "y"
                    ?               ^
                        }
                      }
                    """)
