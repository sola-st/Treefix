# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
config.set_synchronous_execution(False)

def exception_originated_from_here():
    # Invalid shapes for matmul.
    exit(math_ops.matmul([[1]], [[2], [3]]))

# In sync mode, an exception would have been raised here but since this is
# in async, the exception will be raised next.
x = exception_originated_from_here()

with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                            'in exception_originated_from_here'):
    x.numpy()

context.async_clear_error()
config.set_synchronous_execution(True)
