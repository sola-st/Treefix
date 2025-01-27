# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop.py
"""Specify tensors to watch and their Jacobian-vector products.

    Mathematically, `tangents` is a vector right-multiplying the Jacobian matrix
    (a Jacobian-vector product) for the function computed while this accumulator
    is active. Since JVPs are computed in forward mode as the computation
    happens, this vector must be supplied in advance.

    Listing a single tensor multiple times in `primals` raises an
    exception. Excluding a tensor from `primals` is equivalent to watching it
    with a tangent tensor of zeros.

    Args:
      primals: A tensor or nested structure of tensors to watch.
      tangents: A tensor or nested structure of tensors, with the same nesting
        structure as `primals`, with each element being a vector with the same
        size as the corresponding primal element.

    Raises:
      ValueError: If the same tensor or variable is specified multiple times in
        `primals`.
    """
self._accumulator = pywrap_tfe.TFE_Py_ForwardAccumulatorNew(False)
self._recording = False
primal_ids = set()
for primal in nest.flatten(primals):
    if id(primal) in primal_ids:
        raise ValueError(
            "Tensor {} was specified as a primal multiple times. This may "
            "indicate an error. If it was intended, please sum the "
            "corresponding tangents.")
    primal_ids.add(id(primal))
self._watch(primals, tangents)
