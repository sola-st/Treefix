# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

class Foo(Checkpoint):

    @polymorphic_function.function
    def __call__(self, x):
        exit(x)

f_flexible = Foo()
_ = f_flexible.__call__.get_concrete_function(
    tensor_spec.TensorSpec(shape=[None], dtype=dtypes.int32))
tmp_dir = self.create_tempdir()
save(f_flexible, tmp_dir.full_path)
restored_f_flexible = load(tmp_dir.full_path)

f_fixed_shape = Foo()

with self.assertLogs(level='WARN') as logs:
    restored_f_flexible(constant_op.constant([1], dtypes.int32))
    restored_f_flexible(constant_op.constant([1, 2], dtypes.int32))
    restored_f_flexible(constant_op.constant([1, 2, 3], dtypes.int32))
    restored_f_flexible(constant_op.constant([1, 2, 3, 4], dtypes.int32))
    restored_f_flexible(constant_op.constant([1, 2, 3, 4, 5], dtypes.int32))
    self.assertEmpty(logs.output)

    f_fixed_shape(constant_op.constant([1], dtypes.int32))
    f_fixed_shape(constant_op.constant([1, 2], dtypes.int32))
    f_fixed_shape(constant_op.constant([1, 2, 3], dtypes.int32))
    f_fixed_shape(constant_op.constant([1, 2, 3, 4], dtypes.int32))
    f_fixed_shape(constant_op.constant([1, 2, 3, 4, 5], dtypes.int32))
    self.assertLen(logs.output, 1)
    self.assertIn('Tracing is expensive', logs.output[0])
