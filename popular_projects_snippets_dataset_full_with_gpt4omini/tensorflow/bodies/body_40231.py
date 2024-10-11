# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
raise NotImplementedError(
    "tf.GradientTape.gradients() does not support graph control flow "
    "operations like tf.cond or tf.while at this time. Use tf.gradients() "
    "instead. If you need this feature, please file a feature request at "
    "https://github.com/tensorflow/tensorflow/issues/new"
)
