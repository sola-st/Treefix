# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop.py
"""Ensures that `primals` are being traced by this accumulator.

    Mathematically, `tangents` is a vector right-multiplying the Jacobian matrix
    (a Jacobian-vector product) for the function computed while this accumulator
    is active. Since JVPs are computed in forward mode as the computation
    happens, this vector must be supplied in advance.

    Watching a single tensor multiple times sums each of its `tangents`. Any
    un-watched tensor has zeros for its tangent vector.

    Args:
      primals: A Tensor or list of Tensors.
      tangents: A Tensor or list of Tensors matching `primals`.
    """

def _watch(primal, tangent):
    if not primal.dtype.is_floating:
        logging.log_first_n(
            logging.WARN, "The dtype of the watched primal must be "
            "floating (e.g. tf.float32), got %r", 5, primal.dtype)
    tangent = ops.convert_to_tensor(tangent, dtype=primal.dtype)
    if hasattr(primal, "handle"):
        # Run convert_to_tensor to get the captured handle from whichever
        # function we're running if necessary.
        primal = ops.convert_to_tensor(primal.handle)
    pywrap_tfe.TFE_Py_ForwardAccumulatorWatch(self._accumulator, primal,
                                              tangent)

nest.map_structure(_watch, primals, tangents)
