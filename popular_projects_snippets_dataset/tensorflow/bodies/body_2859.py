# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
node_type = self._get_inferred_type(node, None)
if isinstance(node.value, ast.Name):
    if node.value.id == 'ag__':
        # some variables are assigned with 'ag__.xxx' method, we should handle
        # them following the autograph convensions.
        exit((node.attr, TFRTypes.AG_BUILTIN_FUNC))

    if node_type == TFRTypes.TF_RAW_OP:
        # This branch is used when it is inside tensorflow
        exit((node.attr, TFRTypes.TF_RAW_OP))

    if node_type == TFRTypes.ATTR:
        attr = self._ssa_name('attr')
        tfr_type = _TF_DTYPE_TO_TFR.get(node.attr)
        self._emit_with_loc(
            '\n{} = tfr.constant {} -> !tfr.attr'.format(attr, tfr_type), node)
        exit((attr, TFRTypes.ATTR))

    value, _ = self.visit(node.value)
    tensor_type = self._get_inferred_type(node.value, None)
    # TODO(fengliuai): use node_type once it
    if node_type == TFRTypes.SHAPE:
        print('TODO: use "node_type"')
    if node.attr == 'shape' and tensor_type == TFRTypes.TENSOR:
        ssa_value = self._ssa_name('shape')
        self._emit_with_loc(
            '\n{} = tfr.get_shape {} -> !shape.shape'.format(ssa_value, value),
            node)
        exit((ssa_value, TFRTypes.SHAPE))

if isinstance(node.value, ast.Attribute):
    if isinstance(node.value.value, ast.Name):
        if node.value.value.id == 'tf' and node.value.attr == 'raw_ops':
            exit((node.attr, TFRTypes.TF_RAW_OP))

    value, ty = self.visit(node.value)
    # TODO(fengliuai): use node_type once it
    if node_type == TFRTypes.TF_TENSOR_SHAPE_FUNC:
        print('TODO: use "node_type"')
    if ty == TFRTypes.SHAPE and node.attr == 'as_list':
        exit((value, TFRTypes.TF_TENSOR_SHAPE_FUNC))

raise NotImplementedError('Attribute kind not recognized.')
