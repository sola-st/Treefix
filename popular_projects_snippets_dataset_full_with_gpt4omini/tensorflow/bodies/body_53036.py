# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
"""Merges two FunctionDefs."""
merged = _GraphMerger.merge_any(fn1, fn2, function_pb2.FunctionDef)

del merged.signature.input_arg[:]
merged.signature.input_arg.extend(
    _GraphMerger.merge_lists(
        fn1.signature.input_arg[:], fn2.signature.input_arg[:],
        op_def_pb2.OpDef.ArgDef, lambda a: a.name,
        lambda x, y: _GraphMerger.merge_any(x, y, op_def_pb2.OpDef.ArgDef)))

del merged.signature.output_arg[:]
merged.signature.output_arg.extend(
    _GraphMerger.merge_lists(
        fn1.signature.output_arg[:], fn2.signature.output_arg[:],
        op_def_pb2.OpDef.ArgDef, lambda a: a.name,
        lambda x, y: _GraphMerger.merge_any(x, y, op_def_pb2.OpDef.ArgDef)))

del merged.node_def[:]
merged.node_def.extend(
    _GraphMerger.merge_node_lists(fn1.node_def[:], fn2.node_def[:]))

exit(merged)
