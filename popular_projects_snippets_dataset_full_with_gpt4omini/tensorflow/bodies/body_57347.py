# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter.py
"""Resizes an input tensor.

    Args:
      input_index: Tensor index of input to set. This value can be gotten from
        the 'index' field in get_input_details.
      tensor_size: The tensor_shape to resize the input to.
      strict: Only unknown dimensions can be resized when `strict` is True.
        Unknown dimensions are indicated as `-1` in the `shape_signature`
        attribute of a given tensor. (default False)

    Raises:
      ValueError: If the interpreter could not resize the input tensor.

    Usage:
    ```
    interpreter = Interpreter(model_content=tflite_model)
    interpreter.resize_tensor_input(0, [num_test_images, 224, 224, 3])
    interpreter.allocate_tensors()
    interpreter.set_tensor(0, test_images)
    interpreter.invoke()
    ```
    """
self._ensure_safe()
# `ResizeInputTensor` now only accepts int32 numpy array as `tensor_size
# parameter.
tensor_size = np.array(tensor_size, dtype=np.int32)
self._interpreter.ResizeInputTensor(input_index, tensor_size, strict)
