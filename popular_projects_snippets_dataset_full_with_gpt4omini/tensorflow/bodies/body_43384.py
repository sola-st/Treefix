# Extracted from ./data/repos/tensorflow/tensorflow/python/util/protobuf/compare_test.py
self.assertAll('medium: {}')
self.assertAll('medium: { smalls: {} }')
self.assertAll('medium: { int32s: 1 smalls: {} }')
self.assertAll('medium: { smalls: { strings: "x" } }')
self.assertAll(
    'medium: { smalls: { strings: "x" } } small: { strings: "y" }')

self.assertSameNotEqual('medium: { smalls: { strings: "x" strings: "y" } }',
                        'medium: { smalls: { strings: "y" strings: "x" } }')
self.assertSameNotEqual(
    'medium: { smalls: { strings: "x" } smalls: { strings: "y" } }',
    'medium: { smalls: { strings: "y" } smalls: { strings: "x" } }')

self.assertSameNotEqual(
    'medium: { smalls: { strings: "x" strings: "y" strings: "x" } }',
    'medium: { smalls: { strings: "y" strings: "x" } }')
self.assertSameNotEqual(
    'medium: { smalls: { strings: "x" } int32s: 0 }',
    'medium: { int32s: 0 smalls: { strings: "x" } int32s: 0 }')

self.assertNone('medium: {}', 'medium: { smalls: { strings: "x" } }', """
                      medium {
                    +   smalls {
                    +     strings: "x"
                    +   }
                      }
                    """)
self.assertNone('medium: { smalls: { strings: "x" } }',
                'medium: { smalls: {} }', """
                      medium {
                        smalls {
                    -     strings: "x"
                        }
                      }
                    """)
self.assertNone('medium: { int32s: 0 }', 'medium: { int32s: 1 }', """
                      medium {
                    -   int32s: 0
                    ?           ^
                    +   int32s: 1
                    ?           ^
                      }
                    """)
