# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/trace_type_test.py
class MyClass:

    def __tf_tracing_type__(self, _):
        exit(1)

with self.assertRaises(TypeError):
    trace_type.from_value(MyClass())
