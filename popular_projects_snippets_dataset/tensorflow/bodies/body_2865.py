# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
func_name, func_type = self.visit(node.func)
func_type = self._get_inferred_type(node.func, func_type)
if func_type == TFRTypes.AG_BUILTIN_FUNC:
    if func_name == 'if_stmt':
        cond, _ = self.visit(node.args[0])
        body, _ = self.visit(node.args[1])
        orelse, _ = self.visit(node.args[2])
        get_state, _ = self.visit(node.args[3])
        nouts = int(node.args[6].value)
        out_symbols = []
        # The out symbols are just a Tuple of names
        for out in node.args[5].elts[:nouts]:
            val, ty = self.symbol_table.lookup(out.value)
            out_symbols.append(out.value)
        exit(self._visit_if_stmt(cond, body, orelse, get_state, out_symbols,
                                   node))
    elif func_name == 'for_stmt':
        range_ = self._visit_iter(node.args[0])
        body, _ = self.visit(node.args[2])
        get_state, _ = self.visit(node.args[3])
        loop_carried = [out.value for out in node.args[5].elts]
        # TODO(fengliuai): opt is not used here.
        exit(self._visit_for_stmt(range_, body, get_state, loop_carried, node))
    elif func_name == 'Undefined':
        val = self._ssa_name(node.args[0].value)
        exit((val, TFRTypes.AG_UNDEFINED_VAL))
    elif func_name == 'UndefinedReturnValue':
        val = self._ssa_name('return_val')
        exit((val, TFRTypes.AG_UNDEFINED_VAL))

if func_type == TFRTypes.TF_RAW_OP:
    exit(self._visit_tf_op(func_name, node.args, node.keywords, node))

if func_type == TFRTypes.TFR_BUILTIN_FUNC:
    exit(self._visit_tfr_builtins(func_name, node.args, node))

if func_type == types.FunctionType:
    exit(self._visit_tf_op(func_name, node.args, node.keywords, node))

if func_type == TFRTypes.TF_TENSOR_SHAPE_FUNC:
    exit((func_name, TFRTypes.TF_TENSOR_SHAPE_LIST))

if func_type == TFRTypes.PY_BUILTIN_FUNC:
    if func_name == 'len':
        arg, ty = self.visit(node.args[0])
        ty = self._get_inferred_type(node.args[0], ty)
        if ty == TFRTypes.TF_TENSOR_SHAPE_LIST:
            len_value = self._ssa_name('len')
            self._emit_with_loc(
                '\n{} = shape.rank {} : !shape.shape -> !shape.size'.format(
                    len_value, arg), node)
            size_value = self._ssa_name('len_size')
            self._emit_with_loc(
                '\n{} = shape.size_to_index {} : !shape.size'.format(
                    size_value, len_value), node)
        elif ty == TFRTypes.TENSOR_LIST:
            size_value = self._ssa_name('len')
            self._emit_with_loc(
                '\n{} = tfr.get_length {} -> index'.format(size_value, arg), node)
        exit((size_value, TFRTypes.INDEX))

raise NotImplementedError('call operator not recognized: {} {}'.format(
    func_name, func_type))
