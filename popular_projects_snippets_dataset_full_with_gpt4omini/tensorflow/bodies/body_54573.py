# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config.py
"""Disables experimental MLIR-Based TensorFlow Compiler Bridge."""
context.context().enable_mlir_bridge = False
