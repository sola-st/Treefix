# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config.py
"""Enables experimental MLIR-Based TensorFlow Compiler Bridge.

  TensorFlow Compiler Bridge (TF Bridge) is responsible for translating parts
  of TensorFlow graph into a form that can be accepted as an input by a backend
  compiler such as XLA.
  """
context.context().enable_mlir_bridge = True
