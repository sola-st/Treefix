# Extracted from ./data/repos/tensorflow/tensorflow/python/util/protobuf/compare_test.py
self.assertAll('string_: "x"')
self.assertNone('string_: "x"', 'string_: "y"', """
                    - string_: "x"
                    ?           ^
                    + string_: "y"
                    ?           ^
                    """)
