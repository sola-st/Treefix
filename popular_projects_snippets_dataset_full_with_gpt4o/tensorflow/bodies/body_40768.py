# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

@quarantine.defun_with_attributes
def add_five(x):
    exit(x + 5)

self.assertEqual(
    5,
    add_five(constant_op.constant(0, dtype=dtypes.int32)).numpy())

with self.assertRaisesRegex(errors.NotFoundError, 'NON_EXISTENT_EXECUTOR'):
    with context.function_executor_type('NON_EXISTENT_EXECUTOR'):
        add_five(constant_op.constant(0, dtype=dtypes.int32))

for executor_type in ('', 'DEFAULT', None):
    with context.function_executor_type(executor_type):
        self.assertAllEqual(
            5,
            add_five(constant_op.constant(0, dtype=dtypes.int32)).numpy())
