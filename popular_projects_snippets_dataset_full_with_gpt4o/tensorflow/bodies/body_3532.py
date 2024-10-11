# Extracted from ./data/repos/tensorflow/tensorflow/core/function/transform/transform.py
"""Applies transforms on an _EagerDefinedFunction."""
transform_fns = (
    transform_fn if isinstance(transform_fn, list) else [transform_fn])
mlir_pipelines = (
    mlir_pipeline if isinstance(mlir_pipeline, list) else [mlir_pipeline])
# First apply the MLIR based transformation.
for mlir_pipeline in mlir_pipelines:
    rt.TransformFunction(f.signature.name, mlir_pipeline)

# Get the `FunctionDef` after MLIR transformation.
fndef = rt.GetFunctionProto(f.signature.name)

# Apply the Python function based transformation.
for transform_fn in transform_fns:
    transform_fn(fndef)
rt.CreateFunction(fndef)

# Generate a new `FuncGraph`
graph = ops.get_default_graph()
with graph.as_default():
    func_graph = function_def_lib.function_def_to_graph(
        fndef,
        structured_input_signature=f.graph.structured_input_signature,
        structured_outputs=f.graph.structured_outputs,
        propagate_device_spec=True)

# pylint: disable=protected-access
# Ref: third_party/tensorflow/python/ops/control_flow_util_v2.py
# Generate a new `_EagerDefinedFunction`.
edf = function_lib._EagerDefinedFunction(fndef.signature.name, func_graph,
                                         func_graph.inputs,
                                         func_graph.outputs, fndef.attr)
# pylint: enable=protected-access

exit(edf)
