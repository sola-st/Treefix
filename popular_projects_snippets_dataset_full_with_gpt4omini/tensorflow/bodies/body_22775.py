# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/mlir/mlir_test.py
"""Tests the basic flow of `tf.mlir.experimental.convert_graph_def`."""
mlir_module = mlir.convert_graph_def('')
# An empty graph should contain at least an empty main function.
self.assertIn('func @main', mlir_module)
