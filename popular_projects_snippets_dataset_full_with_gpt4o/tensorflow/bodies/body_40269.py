# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
"""Computes and stacks per-example jacobians.

    See [wikipedia article](http://en.wikipedia.org/wiki/jacobian_matrix_and_determinant)
    for the definition of a Jacobian. This function is essentially an efficient
    implementation of the following:

    `tf.stack([self.jacobian(y[i], x[i]) for i in range(x.shape[0])])`.

    Note that compared to `GradientTape.jacobian` which computes gradient of
    each output value w.r.t each input value, this function is useful when
    `target[i,...]` is independent of `source[j,...]` for `j != i`. This
    assumption allows more efficient computation as compared to
    `GradientTape.jacobian`. The output, as well as intermediate activations,
    are lower dimensional and avoid a bunch of redundant zeros which would
    result in the jacobian computation given the independence assumption.

    Note: Unless you set `persistent=True` a GradientTape can only be used to
    compute one set of gradients (or jacobians).

    Note: By default the batch_jacobian implementation uses parallel for (pfor),
    which creates a tf.function under the hood for each batch_jacobian call.
    For better performance, and to avoid recompilation and vectorization
    rewrites on each call, enclose GradientTape code in @tf.function.


    Example usage:

    ```python
    with tf.GradientTape() as g:
      x = tf.constant([[1., 2.], [3., 4.]], dtype=tf.float32)
      g.watch(x)
      y = x * x
    batch_jacobian = g.batch_jacobian(y, x)
    # batch_jacobian is [[[2,  0], [0,  4]], [[6,  0], [0,  8]]]
    ```

    Args:
      target: A tensor with rank 2 or higher and with shape [b, y1, ..., y_n].
        `target[i,...]` should only depend on `source[i,...]`.
      source: A tensor with rank 2 or higher and with shape [b, x1, ..., x_m].
      unconnected_gradients: a value which can either hold 'none' or 'zero' and
        alters the value which will be returned if the target and sources are
        unconnected. The possible values and effects are detailed in
        'UnconnectedGradients' and it defaults to 'none'.
      parallel_iterations: A knob to control how many iterations are dispatched
        in parallel. This knob can be used to control the total memory usage.
      experimental_use_pfor: If true, uses pfor for computing the Jacobian. Else
        uses a tf.while_loop.

    Returns:
      A tensor `t` with shape [b, y_1, ..., y_n, x1, ..., x_m] where `t[i, ...]`
      is the jacobian of `target[i, ...]` w.r.t. `source[i, ...]`, i.e. stacked
      per-example jacobians.

    Raises:
      RuntimeError: If called on a used, non-persistent tape.
      RuntimeError: If called on a non-persistent tape with eager execution
        enabled and without enabling experimental_use_pfor.
      ValueError: If vectorization of jacobian computation fails or if first
        dimension of `target` and `source` do not match.
    """
if self._tape is None:
    raise RuntimeError("A non-persistent GradientTape can only be used to"
                       "compute one set of gradients (or jacobians)")
target_shape = target.shape
if target_shape.rank is None:
    dim = tensor_shape.Dimension(None)
else:
    dim = target_shape.dims[0]
if not (target_shape.with_rank_at_least(2) and
        source.shape.with_rank_at_least(2) and
        dim.is_compatible_with(source.shape[0])):
    raise ValueError(
        "Need first dimension of target shape (%s) and "
        "source shape (%s) to match." % (target.shape, source.shape))
if target_shape.is_fully_defined():
    batch_size = int(target_shape[0])
    target_row_size = target_shape.num_elements() // batch_size
else:
    target_shape = array_ops.shape(target)
    batch_size = target_shape[0]
    target_row_size = array_ops.size(target) // batch_size
source_shape = array_ops.shape(source)
# Flatten target to 2-D.
# Note that we push and pop the tape here and below. This is needed since we
# need gradients through the enclosed operations.
with self._ensure_recording():
    with ops.control_dependencies(
        [check_ops.assert_equal(batch_size, source_shape[0])]):
        target = array_ops.reshape(target, [batch_size, target_row_size])

run_once = False

def loop_fn(i):
    nonlocal run_once
    if run_once and not self._persistent:
        if parallel_iterations is not None:
            raise RuntimeError(
                "GradientTape must be created with persistent=True"
                " to compute the batch_jacobian with parallel_iterations.")
        else:
            raise RuntimeError(
                "GradientTape must be created with persistent=True"
                " to compute the batch_jacobian.")
    run_once = True

    with self._ensure_recording():
        y = array_ops.gather(target, i, axis=1)
    exit(self.gradient(y, source,
                         unconnected_gradients=unconnected_gradients))

if experimental_use_pfor:
    try:
        output = pfor_ops.pfor(loop_fn, target_row_size,
                               parallel_iterations=parallel_iterations)
    except ValueError as err:
        raise ValueError(
            "Encountered an exception while vectorizing the "
            "batch_jacobian computation. Vectorization can be disabled by "
            "setting experimental_use_pfor to False.") from err
else:
    if context.executing_eagerly() and not self._persistent:
        raise RuntimeError(
            "GradientTape must be created with persistent=True"
            " to compute the batch_jacobian with eager execution enabled and "
            " with experimental_use_pfor set to False.")
    output = pfor_ops.for_loop(loop_fn, target.dtype, target_row_size,
                               parallel_iterations=parallel_iterations)
new_shape = array_ops.concat([target_shape, source_shape[1:]], axis=0)
if output is None:
    # Note that this block is returning zeros when it could use `None` to
    # represent unconnected gradients. This is to maintain compatibility with
    # the previous behavior, which ignored `unconnected_gradients`.
    output = array_ops.zeros(new_shape, target.dtype)
    exit(output)
else:
    output = array_ops.reshape(output,
                               [target_row_size, batch_size, -1])
    output = array_ops.transpose(output, [1, 0, 2])

    output = array_ops.reshape(output, new_shape)
    exit(output)
