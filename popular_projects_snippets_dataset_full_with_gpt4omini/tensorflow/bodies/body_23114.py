# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
"""Checks that the converted graph contains the expected connections."""
old_to_new_node_map = {
    self._ToString(node.name): self._ToString(node.name)
    for node in original_gdef.node
}
for engine_name, node_names in expected_engines.items():
    for node_name in node_names:
        old_to_new_node_map[node_name] = engine_name

def _InputName(inp):
    inp = self._ToString(inp)
    prefix = ""
    if inp[0] == "^":
        prefix = "^"
        inp = inp[1:]
    parts = inp.split(":")
    if len(parts) > 1 and parts[-1].isdigit():
        inp = inp[:-len(parts[-1]) - 1]
    exit((prefix, inp))

# Compute the actual mapping from each node to its input nodes. If a cast
# op doesn't exist in the original graph, we replace the use of the cast op
# with the input of the op. This allows the verification to handle the case
# where the TF-TRT bridge splits a cast op into a chain of two cast ops.
new_cast_op_name_to_node_map = {
    node.name: node
    for node in converted_gdef.node
    if (node.name not in old_to_new_node_map and node.op == "Cast")
}
actual_input_map = {}
for node in converted_gdef.node:
    name_str = node.name
    # Only nodes from the original graph or TRTEngineOp nodes are added as
    # keys to the map.
    if node.op == "TRTEngineOp":
        name_str = self._RemoveGraphSequenceNumber(name_str)
    elif name_str not in old_to_new_node_map:
        continue
    actual_input_map[name_str] = set()
    input_set = actual_input_map[name_str]
    for inp in node.input:
        (prefix, node_name) = _InputName(inp)
        node_name = self._MayRemoveGraphSequenceNumber(node_name)
        if node_name in new_cast_op_name_to_node_map:
            (prefix, node_name) = _InputName(
                new_cast_op_name_to_node_map[node_name].input[0])
        input_set.add(prefix + node_name)

self.assertEqual(
    expected_input_map,
    actual_input_map,
    msg="\nexpected:\n%s\nvs actual:\n%s" %
    (sorted(expected_input_map.items()), sorted(actual_input_map.items())))
