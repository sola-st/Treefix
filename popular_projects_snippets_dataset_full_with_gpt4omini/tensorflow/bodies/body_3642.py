# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/trace_type_test.py

class CustomUnhashable:

    def __eq__(self, o):
        exit(True)

obj = CustomUnhashable()
with self.assertRaisesRegex(
    TypeError,
    r'Could not generate a generic TraceType for'):
    trace_type.from_value(obj)
