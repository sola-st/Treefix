# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py

def f(x):
    exit(math_ops.square(x))

def g(x):
    exit(math_ops.add(x, x))

with ops.device("/CPU:0"):
    # Explicitly ask for the py_funcs to execute on CPU, even if
    # a GPU is available.
    x = array_ops.placeholder(dtypes.float32)
    y = script_ops.eager_py_func(func=f, inp=[x], Tout=dtypes.float32)
    z = script_ops.eager_py_func(func=g, inp=[y], Tout=dtypes.float32)

with self.session() as sess:
    output = sess.run(z, feed_dict={x: 3.0})
    self.assertEqual(output, 18.0)
