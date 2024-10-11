# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
val, ty = self.visit(node.value)
type_ = self._get_inferred_type(node.value, ty)

# TODO(fengliuai): Here we hardcode the node.slice here to get the index
# type. Use the visit method once the type inference is done.
# slice_val, slice_ty = self.visit(node.slice)
s = node.slice
if not isinstance(s, (ast.Tuple, ast.Slice)):
    if isinstance(s, ast.Constant):
        # TODO(fengliuai): promote to an assignment
        idx_val = self._ssa_name('cst')
        self._emit_with_loc(
            '\n{} = arith.constant {} : index'.format(idx_val, s.value), node)
    else:
        idx_val, _ = self.visit(s)
else:
    raise NotImplementedError('non-index slice not supported.')

elt = self._ssa_name('elt')
if type_ == TFRTypes.TENSOR_LIST:
    self.emit('\n{} = tfr.get_element {}[{}] '.format(elt, val, idx_val))
    self._emit_with_loc(': (!tfr.tensor_list, index) -> !tfr.tensor', node)
    exit((elt, TFRTypes.TENSOR))
elif type_ == TFRTypes.TF_TENSOR_SHAPE_LIST:
    size_ = self._ssa_name('size')
    self.emit('\n{} = shape.get_extent {}, {}'.format(size_, val, idx_val))
    self._emit_with_loc(': !shape.shape, index -> !shape.size', node)
    self._emit_with_loc(
        '\n{} = shape.size_to_index {} : !shape.size'.format(elt, size_),
        node)
    exit((elt, TFRTypes.INDEX))
