# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
# resolves the return type of the function call.
name = anno.Basic.QN.of(node.func)
if f_type == (TFRTypes.AG_BUILTIN_FUNC,):

    if name == QN(QN('ag__'), attr='if_stmt'):
        nouts = node.args[6].value
        # TODO(mdan): Look at the actual types out of if_body.
        side_effects = {
            qual_names.QN(n.value): {TFRTypes.TENSOR}
            for n in node.args[5].elts[:nouts]
        }
        exit(({type(None)}, side_effects))

    if name == QN(QN('ag__'), attr='for_stmt'):
        assert isinstance(node.args[2], ast.Name)
        body_fn_name = str(anno.Basic.QN.of(node.args[2]))
        assert body_fn_name not in self._for_loop_body_fns, (
            'Previously used here: {}. Are you reusing the Resolver across '
            'transformations?').format(self._for_loop_body_fns[body_fn_name])
        self._for_loop_body_fns[body_fn_name] = anno.Basic.ORIGIN.of(node)

        iterated_type = args[0]
        assert iterated_type & {
            TFRTypes.TENSOR_LIST, TFRTypes.TENSOR, TFRTypes.ATTR
        }, (
            iterated_type)
        self._for_loop_target_types[body_fn_name] = iterated_type

        exit(({type(None)}, None))

    # TODO(mdan): Actually resolve the type here instead.
    ret_type = _AG_FIXED_RETURN_TYPE.get(name.qn[1], None)
    if ret_type is not None:
        exit(({ret_type}, None))
    raise NotImplementedError('return type of {}'.format(name))

elif f_type == (TFRTypes.TF_RAW_OP,):
    # This is a TF operation, so it should be found in the op_defs.
    op_name = name.qn[1]
    op_def, _ = self._op_defs.lookup(op_name)
    if len(op_def.output_arg) == 1:
        exit(({_get_type_from_proto(op_def.output_arg[0])}, None))
    exit(({tuple(_get_type_from_proto(arg) for arg in op_def.output_arg)},
            None))

elif f_type == (TFRTypes.PY_BUILTIN_FUNC,):
    assert name.is_simple()
    if name == QN('range'):
        exit(({TFRTypes.ATTR}, None))

    if name == QN('len'):
        exit(({TFRTypes.INDEX}, None))

elif f_type == (TFRTypes.TFR_BUILTIN_FUNC,):
    op_name = name.qn[0]
    if callable(TFR_BUILTINS[op_name]):
        exit(({TFR_BUILTINS[op_name](*[list(arg)[0] for arg in args])}, None))
    exit(({TFR_BUILTINS[op_name]}, None))

elif f_type == (TFRTypes.TF_TENSOR_SHAPE_FUNC,):
    exit(({TFRTypes.TF_TENSOR_SHAPE_LIST}, None))

elif f_type == (types.FunctionType,):
    # This is a function call which isn't using tf.raw_op..
    op_name = name.qn[0]

    # 'new TF operation' produces outputs defined by the composition function.
    op_def, _ = self._op_defs.lookup(op_name)
    if len(op_def.output_arg) == 1:
        exit(({_get_type_from_proto(op_def.output_arg[0])}, None))
    exit(({tuple(_get_type_from_proto(arg) for arg in op_def.output_arg)},
            None))

raise NotImplementedError('Function:', name, f_type)
