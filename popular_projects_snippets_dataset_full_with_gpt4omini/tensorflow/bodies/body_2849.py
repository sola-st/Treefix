# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
"""Emit the mlir operation with the location associated with the node.

    Args:
      op_str: The mlir operation string to be emitted.
      node: The node of the AST tree, the mlir operation translated from.
    """
loc = ''
if node:
    loc = self._create_mlir_loc(
        anno.getanno(node, anno.Basic.ORIGIN, default=None))
self.emit(op_str + ' ' + loc)
