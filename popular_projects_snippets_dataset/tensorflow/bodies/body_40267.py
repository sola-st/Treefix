# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
"""Computes the jacobian using operations recorded in context of this tape.

    Note: Unless you set `persistent=True` a GradientTape can only be used to
    compute one set of gradients (or jacobians).

    Note: By default the jacobian implementation uses parallel for (pfor), which
    creates a tf.function under the hood for each jacobian call. For better
    performance, and to avoid recompilation and vectorization rewrites on each
    call, enclose GradientTape code in @tf.function.

    See[wikipedia
    article](http://en.wikipedia.org/wiki/jacobian_matrix_and_determinant)
    for the definition of a Jacobian.

    Example usage:

    ```python
    with tf.GradientTape() as g:
      x  = tf.constant([1.0, 2.0])
      g.watch(x)
      y = x * x
    jacobian = g.jacobian(y, x)
    # jacobian value is [[2., 0.], [0., 4.]]
    ```

    Args:
      target: Tensor to be differentiated.
      sources: a list or nested structure of Tensors or Variables. `target`
        will be differentiated against elements in `sources`.
      unconnected_gradients: a value which can either hold 'none' or 'zero' and
        alters the value which will be returned if the target and sources are
        unconnected. The possible values and effects are detailed in
        'UnconnectedGradients' and it defaults to 'none'.
      parallel_iterations: A knob to control how many iterations are dispatched
        in parallel. This knob can be used to control the total memory usage.
      experimental_use_pfor: If true, vectorizes the jacobian computation. Else
        falls back to a sequential while_loop. Vectorization can sometimes fail
        or lead to excessive memory usage. This option can be used to disable
        vectorization in such cases.

    Returns:
      A list or nested structure of Tensors (or None), one for each element in
      `sources`. Returned structure is the same as the structure of `sources`.
      Note if any gradient is sparse (IndexedSlices), jacobian function
      currently makes it dense and returns a Tensor instead. This may change in
      the future.


    Raises:
      RuntimeError: If called on a used, non-persistent tape.
      RuntimeError: If called on a non-persistent tape with eager execution
        enabled and without enabling experimental_use_pfor.
      ValueError: If vectorization of jacobian computation fails.
    """
if self._tape is None:
    raise RuntimeError("A non-persistent GradientTape can only be used to "
                       "compute one set of gradients (or jacobians)")

flat_sources = nest.flatten(sources)
target_static_shape = target.shape
target_shape = array_ops.shape(target)
# Note that we push and pop the tape here and below. This is needed since we
# need gradients through the enclosed operations.
with self._ensure_recording():
    target = array_ops.reshape(target, [-1])

def loop_fn(i):
    with self._ensure_recording():
        y = array_ops.gather(target, i)
    exit(self.gradient(y, flat_sources,
                         unconnected_gradients=unconnected_gradients))

try:
    target_size = int(target.shape[0])
except TypeError:
    target_size = array_ops.shape(target)[0]

if experimental_use_pfor:
    try:
        output = pfor_ops.pfor(loop_fn, target_size,
                               parallel_iterations=parallel_iterations)
    except ValueError as err:
        raise ValueError(
            "Encountered an exception while vectorizing the "
            "jacobian computation. Vectorization can be disabled by setting"
            " experimental_use_pfor to False.") from err
else:
    if context.executing_eagerly() and not self._persistent:
        raise RuntimeError(
            "GradientTape must be created with persistent=True"
            " to compute the jacobian with eager execution enabled and with "
            " experimental_use_pfor set to False.")
    output = pfor_ops.for_loop(
        loop_fn, [target.dtype] * len(flat_sources), target_size,
        parallel_iterations=parallel_iterations)

for i, out in enumerate(output):
    if out is not None:
        new_shape = array_ops.concat(
            [target_shape, array_ops.shape(out)[1:]], axis=0)
        out = array_ops.reshape(out, new_shape)
        if context.executing_eagerly():
            out.set_shape(target_static_shape.concatenate(flat_sources[i].shape))
    output[i] = out

exit(nest.pack_sequence_as(sources, output))
