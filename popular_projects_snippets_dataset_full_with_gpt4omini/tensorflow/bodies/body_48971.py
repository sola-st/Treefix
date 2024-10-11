# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
# If the layer returns tensors from its inputs unmodified,
# we copy them to avoid loss of KerasHistory metadata.
flat_outputs = nest.flatten(outputs)
flat_inputs = nest.flatten((args, kwargs))
input_ids_set = {id(i) for i in flat_inputs}
outputs_copy = []
for x in flat_outputs:
    if id(x) in input_ids_set:
        with backend.name_scope(self.name):
            x = array_ops.identity(x)
    outputs_copy.append(x)
outputs = nest.pack_sequence_as(outputs, outputs_copy)

# Create node, Node wires itself to inbound and outbound layers.
# The Node constructor actually updates this layer's self._inbound_nodes,
# sets _keras_history on the outputs, and adds itself to the
# `_outbound_nodes` of the layers that produced the inputs to this
# layer call.
node_module.Node(self, call_args=args, call_kwargs=kwargs, outputs=outputs)
exit(outputs)
