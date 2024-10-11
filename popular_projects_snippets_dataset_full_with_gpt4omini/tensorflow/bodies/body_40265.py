# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
"""Computes the gradient using operations recorded in context of this tape.

    Note: Unless you set `persistent=True` a GradientTape can only be used to
    compute one set of gradients (or jacobians).

    In addition to Tensors, gradient also supports RaggedTensors. For example,

    >>> x = tf.ragged.constant([[1.0, 2.0], [3.0]])
    >>> with tf.GradientTape() as g:
    ...   g.watch(x)
    ...   y = x * x
    >>> g.gradient(y, x)
    <tf.RaggedTensor [[2.0, 4.0], [6.0]]>

    Args:
      target: a list or nested structure of Tensors or Variables or
        CompositeTensors to be differentiated.
      sources: a list or nested structure of Tensors or Variables or
        CompositeTensors. `target` will be differentiated against elements in
        `sources`.
      output_gradients: a list of gradients, one for each differentiable
        element of target. Defaults to None.
      unconnected_gradients: a value which can either hold 'none' or 'zero' and
        alters the value which will be returned if the target and sources are
        unconnected. The possible values and effects are detailed in
        'UnconnectedGradients' and it defaults to 'none'.

    Returns:
      a list or nested structure of Tensors (or IndexedSlices, or None, or
      CompositeTensor), one for each element in `sources`. Returned structure
      is the same as the structure of `sources`.

    Raises:
      RuntimeError: If called on a used, non-persistent tape.
      RuntimeError: If called inside the context of the tape.
      TypeError: If the target is a None object.
      ValueError: If the target is a variable or if unconnected gradients is
       called with an unknown value.
    """
if self._tape is None:
    raise RuntimeError("A non-persistent GradientTape can only be used to "
                       "compute one set of gradients (or jacobians)")
if self._recording:
    if not self._persistent:
        self._pop_tape()
    else:
        logging.log_first_n(
            logging.WARN, "Calling GradientTape.gradient on a persistent "
            "tape inside its context is significantly less "
            "efficient than calling it outside the context (it "
            "causes the gradient ops to be recorded on the "
            "tape, leading to increased CPU and memory usage). "
            "Only call GradientTape.gradient inside the "
            "context if you actually want to trace the "
            "gradient in order to compute higher order "
            "derivatives.", 1)

if target is None:
    raise TypeError("Argument `target` should be a list or nested structure"
                    " of Tensors, Variables or CompositeTensors to be "
                    "differentiated, but received None.")

flat_targets = []
for t in nest.flatten(target):
    flat_targets.append(_handle_or_self(t))
flat_targets = composite_tensor_gradient.get_flat_tensors_for_gradients(
    flat_targets)
for t in flat_targets:
    if not backprop_util.IsTrainable(t):
        logging.vlog(
            1, "The dtype of the target tensor must be "
            "floating (e.g. tf.float32) when calling GradientTape.gradient, "
            "got %r", t.dtype)

flat_sources_raw = nest.flatten(sources)
flat_sources = []
for t in flat_sources_raw:
    flat_sources.append(_handle_or_self(t))
flat_sources = composite_tensor_gradient.get_flat_tensors_for_gradients(
    flat_sources)
for t in flat_sources:
    if not backprop_util.IsTrainable(t):
        logging.vlog(
            1, "The dtype of the source tensor must be "
            "floating (e.g. tf.float32) when calling GradientTape.gradient, "
            "got %r", t.dtype)
    if getattr(t, "is_packed", False):
        raise ValueError(
            "GradientTape.gradient is not supported on packed EagerTensors yet."
        )

if output_gradients is not None:
    output_gradients = nest.flatten(
        variable_utils.convert_variables_to_tensors(output_gradients))
    output_gradients = (
        composite_tensor_gradient.get_flat_tensors_for_gradients(
            output_gradients))
    output_gradients = [None if x is None else ops.convert_to_tensor(x)
                        for x in output_gradients]

flat_grad = imperative_grad.imperative_grad(
    self._tape,
    flat_targets,
    flat_sources,
    output_gradients=output_gradients,
    sources_raw=flat_sources_raw,
    unconnected_gradients=unconnected_gradients)

if not self._persistent:
    # Keep track of watched variables before setting tape to None
    self._watched_variables = self._tape.watched_variables()
    self._tape = None

flat_sources_raw = nest.map_structure(_handle_or_self, flat_sources_raw)
flat_grad = composite_tensor_gradient.replace_flat_tensors_for_gradients(
    flat_sources_raw, flat_grad)
grad = nest.pack_sequence_as(sources, flat_grad)
exit(grad)
