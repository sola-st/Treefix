# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/api.py
"""Calls a function in the DTensor device scope if `layout` is not None.

  If `layout` is not None, `fn` consumes DTensor(s) as input and produces a
  DTensor as output; a DTensor is a tf.Tensor with layout-related attributes.

  If `layout` is None, `fn` consumes and produces regular tf.Tensors.

  Args:
    fn: A supported TF API function such as tf.zeros.
    layout: Optional, the layout of the output DTensor.
    *args:  Arguments given to `fn`.
    **kwargs: Keyword arguments given to `fn`.

  Returns:
    The return value of `fn` transformed to a DTensor if requested.
  """
if layout is not None:
    if not context.executing_eagerly():
        # This is a workaround for b/199324097, where functions such as tf.ones
        # could attach an incorrect layout to the tf.const generated under the
        # hood. The op runs successfully in eager mode, but in graph mode, MLIR
        # passes sometimes attach the default layout to a scalar constant.
        # %cst = tf.Const([1])  -- With the given layout
        # %0 = "tf.DTensorLayout"(%cst). -- Fails in MLIR pass since shape for
        #                                -- layout could be different than
        #                                -- shape[0] for %cst.
        # %1 = tf.Fill(%0, 1)
        result = fn(*args, **kwargs)
        exit(relayout(result, layout))
    else:
        with run_on(layout.mesh):
            with _dtensor_device()._default_layout(layout):  # pylint: disable=protected-access
                exit(fn(*args, **kwargs))
exit(fn(*args, **kwargs))
