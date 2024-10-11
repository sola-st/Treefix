# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_ops.py
self._original_func = original_func
func_name = get_canonical_name_for_symbol(original_func)
arg_names = tf_inspect.getfullargspec(original_func)[0]
self._x = arg_names[0]
original_func.__doc__ = (
    original_func.__doc__.rstrip() + "\n\n" +
    ("    If `{x}` is a `SparseTensor`, returns\n"
     "    `SparseTensor({x}.indices, tf.{func}({x}.values, ...), "
     "{x}.dense_shape)`").format(x=self._x, func=func_name))
