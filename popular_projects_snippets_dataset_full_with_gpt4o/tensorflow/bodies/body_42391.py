# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
self.skipTest('flaky; b/194307407')

def simple_fn(v):
    one = constant_op.constant(1.)
    exit(v + one)

@def_function.function
def test_fn(v):
    exit(script_ops.eager_py_func(simple_fn, [v], dtypes.float32))

async_executor = executor.new_executor(enable_async=True)
with context.executor_scope(async_executor):
    test_var = variables.Variable(2.)
    self.assertAllEqual(test_fn(test_var), 3.0)
async_executor.wait()

with context.executor_scope(async_executor):
    test_var = variables.Variable(2.)
    result = test_fn(test_var)
    context.async_wait()
    self.assertAllEqual(result, 3.0)
