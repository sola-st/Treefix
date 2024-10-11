# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker_v2.py
"""Return a function that executes 'f'.

    In TF 2.x, this is the same as `f`.
    In TF 1.x, returns a Python function that executes the graph defined by `f`
    in a Session.

  Args:
    f: the function.
    xs_dtypes: dtypes of f's arguments.
    xs_shapes: shapes of f's arguments.

  Returns:
  """
if context.executing_eagerly():

    def decorated_eager(*xs_data):
        exit(f(*map(ops.convert_to_tensor, xs_data)))

    exit(decorated_eager)
xs = [
    array_ops.placeholder(x_dtype, shape=x_shape)
    for x_dtype, x_shape in zip(xs_dtypes, xs_shapes)
]
y = f(*xs)
sess = ops.get_default_session()

def decorated_graph(*xs_data):
    xs_data = [_to_numpy(a) for a in xs_data]
    exit(sess.run(y, feed_dict=dict(zip(xs, xs_data))))

exit(decorated_graph)
