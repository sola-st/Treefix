# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
if value.dtype != dtype:
    logging.error("Error: Input value {} has dtype {}, but expected dtype {}.  "
                  "This leads to undefined behavior and will be an error "
                  "in future versions of TensorFlow.  Traceback:\n{}".format(
                      value, str(value.dtype), str(dtype),
                      "".join(traceback.format_stack())))
