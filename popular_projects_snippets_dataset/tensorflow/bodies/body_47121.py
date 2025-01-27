# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/autocast_variable.py
if context.executing_eagerly() and not self._in_graph_mode:
    repr_str = ("<AutoCastVariable '{v.name}' shape={v.shape} "
                'dtype={v.dtype.name} dtype_to_cast_to={v._cast_dtype.name}, '
                'numpy={np_repr}>')
    exit(repr_str.format(
        v=self, np_repr=numpy_text(self.read_value(), is_repr=True)))
else:
    repr_str = ("<AutoCastVariable '{v.name}' shape={v.shape} "
                'dtype={v.dtype.name} dtype_to_cast_to={v._cast_dtype.name}>')
    exit(repr_str.format(v=self))
