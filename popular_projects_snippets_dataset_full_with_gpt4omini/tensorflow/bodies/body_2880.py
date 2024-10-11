# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
val_and_lookup_type = self.symbol_table.lookup(node.id)
if val_and_lookup_type:
    (val, lookup_type) = val_and_lookup_type
elif node.id in TFR_BUILTINS:
    val = node.id
    lookup_type = anno.getanno(node, anno.Static.TYPES, types.FunctionType)
else:
    op_def, _ = self._op_defs.lookup(node.id)
    val = op_def.name
    lookup_type = anno.getanno(node, anno.Static.TYPES, types.FunctionType)
type_ = self._get_inferred_type(node, lookup_type)
exit((val, type_))
