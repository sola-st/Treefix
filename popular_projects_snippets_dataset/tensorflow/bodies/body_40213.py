# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop.py
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
