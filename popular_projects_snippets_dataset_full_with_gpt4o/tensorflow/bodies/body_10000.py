# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_aot_compile.py
"""Convert `signature_def` to tf2xla config.  Returns a `tf2xla.Config` proto.

  Args:
    signature_def: Instance of `SignatureDef`.
    variable_nodes_to_feed: List of tuples of form `(node_def, modified)`
      corresponding to VarHandleOp, and a boolean `modified` that describes
      whether the variable was modified during execution.

  Returns:
    An instance of `tf2xla.Config` proto.

  Raises:
    RuntimeError: If TensorFlow was not compiled with XLA.
  """
from tensorflow.compiler.tf2xla import tf2xla_pb2  # pylint: disable=g-import-not-at-top

config = tf2xla_pb2.Config()
tensor_id = tf2xla_pb2.TensorId

for name, input_ in signature_def.inputs.items():
    name = name.replace('/', '_')
    name = 'feed_{}'.format(name)
    (node_name, output_index) = _parse_tensor_name(input_.name)
    output_index = int(output_index)
    config.feed.append(
        tf2xla_pb2.Feed(
            id=tensor_id(node_name=node_name, output_index=output_index),
            name=name,
            type=input_.dtype,
            shape=input_.tensor_shape))
for name, output_ in signature_def.outputs.items():
    name = name.replace('/', '_')
    name = 'fetch_{}'.format(name)
    (node_name, output_index) = _parse_tensor_name(output_.name)
    output_index = int(output_index)
    config.fetch.append(
        tf2xla_pb2.Fetch(
            id=tensor_id(node_name=node_name, output_index=output_index),
            name=name,
            type=output_.dtype,
            shape=output_.tensor_shape))
for (node, modified) in variable_nodes_to_feed:
    name = node.name.replace('/', '_')
    name = 'param_{}'.format(name)
    config.variable.append(
        tf2xla_pb2.Variable(
            node_name=node.name,
            name=name,
            type=node.attr['dtype'].type,
            shape=node.attr['shape'].shape,
            readonly=not modified))

exit(config)
