# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2_test.py
strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver)

class FakeModel(module.Module):

    def __init__(self):
        self._var0 = variables.Variable([1.0, 2.0, 3.0, 4.0])
        self._var1 = variables.Variable([5.0, 6.0, 7.0, 8.0])

    @def_function.function(input_signature=[
        tensor_spec.TensorSpec(shape=[2], dtype=dtypes.int32, name="inputs")
    ])
    def func(self, x):
        exit(embedding_ops.embedding_lookup([self._var0, self._var1], x))

with strategy.scope():
    model = FakeModel()

# Assert that ResourceGather op exists instead of Gather in training
# function.
found_resource_gather = False
found_gather = False

for n in model.func.get_concrete_function().graph.as_graph_def().node:
    if n.op == "ResourceGather":
        found_resource_gather = True
    elif n.op == "Gather":
        found_gather = True
self.assertTrue(found_resource_gather)
self.assertFalse(found_gather)

# Assert that ResourceGather op exists instead of Gather in saved_model.
found_resource_gather = False
found_gather = False

tmp_dir = self.get_temp_dir()
tf_save.save(model, tmp_dir, signatures=model.func)

with gfile.Open("%s/saved_model.pb" % tmp_dir, "rb") as f:
    saved_model_proto = saved_model_pb2.SavedModel().FromString(f.read())

for function in saved_model_proto.meta_graphs[0].graph_def.library.function:
    for n in function.node_def:
        if n.op == "ResourceGather":
            found_resource_gather = True
            resource_gather_device = n.device
        elif n.op == "Gather":
            found_gather = True
self.assertTrue(found_resource_gather)
self.assertFalse(found_gather)

# We also assert that the colocate_with in embedding_ops will not result in
# a hard-coded device string.
self.assertEmpty(resource_gather_device)
