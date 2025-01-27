# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_utils.py
"""Helper method for `create_keras_history`.

  Args:
    tensors: A structure of Tensors for which to create Keras metadata.
    processed_ops: Set. TensorFlow operations that have already been wrapped in
      `TensorFlowOpLayer` instances.
    created_layers: List. The `TensorFlowOpLayer` instances created.

  Returns:
    Tuple. First element is the updated set of TensorFlow Operations that
    have been wrapped in `TensorFlowOpLayer` instances. Second element is
    a list of the `TensorFlowOpLayer` instances created.
  """
if ops.executing_eagerly_outside_functions():
    raise ValueError(
        '`create_keras_history` should only be called if eager is disabled!')
# Import of `base_layer` needed in order to create `TensorFlowOpLayer`.
# Cannot be imported at top because of circular dependencies.
# TODO(omalleyt): Resolve circular dependency.
from tensorflow.python.keras.engine import base_layer  # pylint: disable=g-import-not-at-top
tensor_list = nest.flatten(tensors)
sparse_ops = []
ragged_tensors = []
for tensor in tensor_list:
    if getattr(tensor, '_keras_history', None) is not None:
        continue
    if isinstance(
        tensor, (sparse_tensor.SparseTensor, sparse_tensor.SparseTensorValue)):
        sparse_ops.append(tensor.op)
        continue
    if tf_utils.is_ragged(tensor):
        # Ragged tensors don't have an op property
        ragged_tensors.append(tensor)
        continue
    op = tensor.op  # The Op that created this Tensor.
    if op not in processed_ops:
        # Recursively set `_keras_history`.
        op_inputs = list(op.inputs)
        constants = {}
        layer_inputs = []
        for i, op_input in enumerate(op_inputs):
            if uses_keras_history(op_input):
                layer_inputs.append(op_input)
            else:
                # Treat any value not originating from a `keras.Input` as
                # a constant. Variables cannot be supported.
                ds_with_session = (
                    distribution_strategy_context.in_cross_replica_context() and
                    not ops.executing_eagerly_outside_functions())
                using_xla = control_flow_util.GraphOrParentsInXlaContext(
                    ops.get_default_graph())
                if ds_with_session or using_xla or _UNSAFE_GRAPH_OP_LAYER_CREATION:
                    # In Legacy Graph mode, evaluating here makes Session be
                    # configured improperly. The downside of this is that saving
                    # via `get_config` breaks, but SavedModel still works.
                    constants[i] = op_input
                else:
                    with ops.init_scope():
                        constants[i] = backend.function([], op_input)([])
        layer_inputs = unnest_if_single_tensor(layer_inputs)
        processed_ops, created_layers = _create_keras_history_helper(
            layer_inputs, processed_ops, created_layers)
        name = op.name
        node_def = op.node_def.SerializeToString()
        op_layer = base_layer.TensorFlowOpLayer(
            node_def, constants=constants, name=name)
        created_layers.append(op_layer)
        op_layer._set_connectivity_metadata(  # pylint: disable=protected-access
            args=(layer_inputs,),
            kwargs={},
            outputs=op.outputs)
        processed_ops.update([op])
if sparse_ops or ragged_tensors:
    lambda_example = """
    weights_mult = lambda x: tf.sparse.sparse_dense_matmul(x, weights)
    output = tf.keras.layers.Lambda(weights_mult)(input)
    """
    raise ValueError(
        'Tensorflow ops that generate ragged or sparse tensor '
        'outputs are currently not supported by Keras automatic '
        'op wrapping. Please wrap these ops in a Lambda layer: '
        '\n\n```\n{example}\n```\n'
        'Sparse ops encountered: {sparse_ops}\n'
        'Ragged tensors encountered: {ragged_tensors}\n'.format(
            example=lambda_example,
            sparse_ops=str(sparse_ops),
            ragged_tensors=str(ragged_tensors)))
exit((processed_ops, created_layers))
