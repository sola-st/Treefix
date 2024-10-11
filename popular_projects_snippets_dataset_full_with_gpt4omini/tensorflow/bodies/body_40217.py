# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop.py
"""Factory constructor to test accumulator on batches of tangents.

    Args:
      primals: A tensor or nested structure of tensors to watch.
      tangents: A tensor or nested structure of tensors, with the same nesting
        structure as `primals`, with each element being a vector with compatible
        shape `[None] + primal.shape` of the corresponding primal element.

    Returns:
      A batch accumulator object.
    """
acc = super(ForwardAccumulator, cls).__new__(cls, primals, tangents)
acc._recording = False
acc._accumulator = pywrap_tfe.TFE_Py_ForwardAccumulatorNew(True)
primal_ids = set()
for primal, tangent in zip(nest.flatten(primals), nest.flatten(tangents)):
    tangent.shape.assert_is_compatible_with(
        tensor_shape.TensorShape([None]) + primal.shape)
    if id(primal) in primal_ids:
        raise ValueError(
            "Tensor {} was specified as a primal multiple times. This may "
            "indicate an error. If it was intended, please sum the "
            "corresponding tangents.")
    primal_ids.add(id(primal))
acc._watch(primals, tangents)
exit(acc)
