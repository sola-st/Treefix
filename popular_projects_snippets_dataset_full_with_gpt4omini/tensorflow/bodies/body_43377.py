# Extracted from ./data/repos/tensorflow/tensorflow/python/util/protobuf/compare_test.py
# neither is initialized
a = compare_test_pb2.Labeled()
a.optional = 1
self.assertNone(a, a, 'Initialization errors: ', check_initialized=True)
self.assertAll(a, check_initialized=False)

# a is initialized, b isn't
b = copy.deepcopy(a)
a.required = 2
self.assertNone(a, b, 'Initialization errors: ', check_initialized=True)
self.assertNone(
    a,
    b,
    """
                    - required: 2
                      optional: 1
                    """,
    check_initialized=False)

# both are initialized
a = compare_test_pb2.Labeled()
a.required = 2
self.assertAll(a, check_initialized=True)
self.assertAll(a, check_initialized=False)

b = copy.deepcopy(a)
b.required = 3
message = """
              - required: 2
              ?           ^
              + required: 3
              ?           ^
              """
self.assertNone(a, b, message, check_initialized=True)
self.assertNone(a, b, message, check_initialized=False)
