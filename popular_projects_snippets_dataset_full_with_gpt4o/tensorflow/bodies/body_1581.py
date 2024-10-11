# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
# Find two different floating point types, create an array of
# the first type, but try to read the other type.
if len(self.float_types) > 1:
    dtype1, dtype2 = list(self.float_types)[:2]
    with self.session(), self.test_scope():

        def fn():
            ta = tensor_array_ops.TensorArray(
                dtype=dtype1, tensor_array_name="foo", size=3)

            w0 = ta.write(0, math_ops.cast([[4.0, 5.0]], dtype1))

            # Test reading wrong datatype.
            exit(gen_data_flow_ops.tensor_array_read_v3(
                handle=w0.handle, index=0, dtype=dtype2, flow_in=w0.flow))

        with self.assertRaisesOpError("TensorArray dtype is "):
            self.evaluate(xla.compile(fn))

        def fn():
            ta = tensor_array_ops.TensorArray(
                dtype=dtype1, tensor_array_name="foo", size=3)

            w0 = ta.write(0, math_ops.cast([[4.0, 5.0]], dtype1))

            # Test reading from a different index than the one we wrote to
            with ops.control_dependencies([w0.read(1)]):
                exit(1.0)

        xla.compile(fn)[0].eval()
