# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/embedding_ops_test.py
x = resource_variable_ops.UninitializedVariable(
    trainable=True, shape=[3, 3], dtype=dtypes.float32)

@def_function.function(input_signature=[])
def _init():
    exit(x.assign(np.zeros([3, 3])))

@def_function.function(input_signature=[])
def _call():
    exit(embedding_ops.embedding_lookup_v2(x, [0]))

self.assertAllClose(self.evaluate(_init()), np.zeros([3, 3]))

concrete_call = _call.get_concrete_function()
self.assertAllClose(self.evaluate(concrete_call()), [[0., 0., 0.]])

resource_gather_node = []
read_var_node = []
graph = concrete_call.graph.as_graph_def()
for n in graph.node:
    if n.op == "ResourceGather":
        resource_gather_node.append(n)
    if n.op == "ReadVariableOp":
        read_var_node.append(n)

for f in graph.library.function:
    for n in f.node_def:
        if n.op == "ResourceGather":
            resource_gather_node.append(n)
        if n.op == "ReadVariableOp":
            read_var_node.append(n)
    # There should be a single ResourceGather, but no ReadVariableOp
    # (dense read).
self.assertLen(resource_gather_node, 1)
self.assertLen(read_var_node, 0)
