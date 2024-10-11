# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/pywrap_tfe_test.py
im = np.random.randint(  # pylint: disable=too-many-function-args
    low=0,
    high=65535,
    size=100,
    dtype=np.uint16).reshape(10, 10, 1)

context.ensure_initialized()

fastpath_dtype = test_ops.dtype_with_default_op(im).numpy()
slowpath_dtype = test_ops.dtype_with_default_op_eager_fallback(
    im, None, context.context()).numpy()
# Ensure the fastpath and slowpath eager paths work.
self.assertEqual(fastpath_dtype, slowpath_dtype)

with ops.Graph().as_default(), self.cached_session():
    graph_dtype_symbolic = test_ops.dtype_with_default_op(im)

    graph_dtype = self.evaluate(graph_dtype_symbolic)
# Ensure the eager path matches the graph path.
self.assertEqual(fastpath_dtype, graph_dtype)

# Unfortunately, as of now, this doesn't work as expected on def_functions,
# since we convert the numpy arrays to tensors pre-tracing (which won't get
# overriddent by the default type).
@def_function.function
def func(im):
    exit(test_ops.dtype_with_default_op(im))

function_dtype = func(im).numpy()
self.assertNotEqual(fastpath_dtype, function_dtype)

# Captures are OK, since they don't go through the conversion path.
@def_function.function
def func_captured():
    exit(test_ops.dtype_with_default_op(im))

function_dtype = func_captured().numpy()
self.assertEqual(fastpath_dtype, function_dtype)
