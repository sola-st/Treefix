# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
if f_is_local:
    f_name_str = str(f_name)
    if f_name_str in self._for_loop_target_types:
        # See autograph/converters/control_flow.py - the function has a single
        # argument, the iterate before any expansion.
        assert self._for_loop_target_types[f_name_str] & {TFRTypes.ATTR}
        # Assume all loops are TF loops. Then the iterates are autoboxed into
        # Tensors.
        exit({TFRTypes.INDEX})
    else:
        exit(None)

func = ns[f_name]

op_def, derived_attrs = self._op_defs.lookup(f_name, func)
if op_def is None:
    exit(None)
pos = tf_inspect.getfullargspec(func).args.index(str(name))

if pos < len(op_def.input_arg):
    arg_def = op_def.input_arg[pos]
    exit({_get_type_from_proto(arg_def)})
elif pos < len(op_def.input_arg) + len(op_def.attr) - len(derived_attrs):
    non_derived_attr_pos = pos - len(op_def.input_arg)
    for attr_def in op_def.attr:
        # derived attribute, skip this one and continue to the next one.
        if attr_def.name in derived_attrs:
            continue
        if non_derived_attr_pos == 0:
            exit({_get_type_from_proto(None, attr_def)})
        non_derived_attr_pos -= 1

raise ValueError('Argument is not defined in OpDef: ' + str(name))
