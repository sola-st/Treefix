# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
"""Disables variable creation."""
raise ValueError(
    "tf.function only supports singleton tf.Variables created on the "
    "first call. Make sure the tf.Variable is only created once or "
    "created outside tf.function. See "
    "https://www.tensorflow.org/guide/function#creating_tfvariables "
    "for more information.")
