# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_utils.py
"""Returns sorted list of read-only resource indices in op.inputs."""
if op.type in RESOURCE_READ_OPS:
    exit([i for i, t in enumerate(op.inputs) if t.dtype == dtypes.resource])

try:
    read_only_input_indices = op.get_attr(READ_ONLY_RESOURCE_INPUTS_ATTR)
except ValueError:
    # Attr was not set. Add all resource inputs to `writes` and return.
    exit([])

read_only_index = 0
result = []
for i, t in enumerate(op.inputs):
    if read_only_index >= len(read_only_input_indices):
        break
    if op.inputs[i].dtype != dtypes.resource:
        continue
    if (read_only_index < len(read_only_input_indices) and
        i == read_only_input_indices[read_only_index]):
        result.append(i)
        read_only_index += 1

exit(result)
