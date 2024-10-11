# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
op_def, derived_attrs = self._op_defs.lookup(node.name, node, True)
if op_def is None:
    # Nested function. Insert it to symbol table for looking up later.
    self.symbol_table.insert_symbol(node.name, node, None)
    exit()
op_name = op_def.name
if self.symbol_table.lookup(op_name):
    raise LookupError('Composition has not been registered for op: ' +
                      op_name)
else:
    self.symbol_table.insert_symbol(node.name, None, None)

self.symbol_table.enter_scope()
self.emit('\ntfr.func @tf__{0}('.format(_camel_to_snake(op_name)))

arg_list = []
idx = 0
max_idx = len(op_def.input_arg) + len(op_def.attr)
for arg in node.args.args:
    arg_name = self._ssa_name(anno.getanno(arg, anno.Basic.QN))
    arg_type = anno.getanno(arg, anno.Static.TYPES)[0]

    arg_attr = ''
    if idx >= len(op_def.input_arg):
        attr_def = op_def.attr[idx - len(op_def.input_arg)]
        # skip the derived attributes
        while attr_def.name in derived_attrs and (idx + 1) < max_idx:
            idx += 1
            attr_def = op_def.attr[idx - len(op_def.input_arg)]
        if idx >= max_idx:
            raise ValueError('Argument is not defined in OpDef: ' + arg_name)

        arg_attr += '{{tfr.name="{}"'.format(attr_def.name)
        if attr_def.HasField('default_value'):
            default_val = _get_val_from_proto(arg_type, attr_def.default_value)
            arg_attr += ',tfr.default={}'.format(default_val)
        arg_attr += '}'

    idx += 1
    arg_str = '{}: {}{}'.format(arg_name, arg_type, arg_attr)
    arg_list.append(arg_str)
    self.symbol_table.insert_symbol(arg.id, arg_name, arg_type)

ret_type_list = []
for ret_def in op_def.output_arg:
    if ret_def.number_attr or ret_def.type_list_attr:
        ret_type_list.append(str(TFRTypes.TENSOR_LIST))
    else:
        ret_type_list.append(str(TFRTypes.TENSOR))

self.emit('{}) -> ({}) {{'.format(', '.join(arg_list),
                                  ', '.join(ret_type_list)))
self.visit_block(node.body)
self._emit_with_loc('\n}', node)
self.symbol_table.exit_scope()
