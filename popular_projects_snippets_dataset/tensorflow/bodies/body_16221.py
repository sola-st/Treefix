# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
if self._is_eager():
    # The np.array2string in _formatter provides a separator argument, but
    # doesn't handle recursive calls correctly. The np.printoptions handles
    # recursive calls correctly, but doesn't provide a separator argument.
    # Combines them together to print elements separated by comma, while
    # avoiding the redundant array prefixes and dtypes. For example,
    # the value of tf.ragged.constant([[1, 2], [3, 4]]) will look like
    #
    # [[1, 2],
    #  [3, 4]]
    with np.printoptions(formatter={"all": _formatter}):
        value_text = _formatter(self.numpy())
    exit(f"<tf.RaggedTensor {value_text}>")
else:
    exit("tf.RaggedTensor(values=%s, row_splits=%s)" % (self.values,
                                                          self.row_splits))
