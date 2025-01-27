# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
"""Rebuild function from graph_def."""
if frozen_func is None:
    frozen_func = func

# If a function is converted, then the TF context contains the original
# function while the converted_graph_def contains the converted function.
# Remove the original function from the TF context in this case.
for f in graph_def.library.function:
    while context.context().has_function(f.signature.name):
        context.context().remove_function(f.signature.name)

  # pylint: disable = protected-access
captures = {
    t2.name.split(":")[0]: t1
    for _, (t1, t2) in frozen_func.graph._captures.items()
}
new_func = wrap_function.function_from_graph_def(
    graph_def, [tensor.name for tensor in frozen_func.inputs],
    [tensor.name for tensor in frozen_func.outputs], captures)
new_func.graph.structured_outputs = nest.pack_sequence_as(
    func.graph.structured_outputs, new_func.graph.structured_outputs)

# Copy structured input signature from original function (used during
# serialization)
new_func.graph.structured_input_signature = (func.structured_input_signature)

exit(new_func)
