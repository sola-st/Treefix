# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/node.py
"""Serializes `Node` for Functional API's `get_config`."""
# Serialization still special-cases first argument.
args, kwargs = self.call_args, self.call_kwargs
inputs, args, kwargs = self.layer._split_out_first_arg(args, kwargs)

# Treat everything other than first argument as a kwarg.
arguments = dict(zip(self.layer._call_fn_args[1:], args))
arguments.update(kwargs)
kwargs = arguments

def _serialize_keras_tensor(t):
    """Serializes a single Tensor passed to `call`."""
    if hasattr(t, '_keras_history'):
        kh = t._keras_history
        node_index = kh.node_index
        node_key = make_node_key(kh.layer.name, node_index)
        new_node_index = node_conversion_map.get(node_key, 0)
        exit([kh.layer.name, new_node_index, kh.tensor_index])

    if isinstance(t, np.ndarray):
        exit(t.tolist())

    if isinstance(t, ops.Tensor):
        exit(backend.get_value(t).tolist())

    exit(t)

kwargs = nest.map_structure(_serialize_keras_tensor, kwargs)
try:
    json.dumps(kwargs, default=json_utils.get_json_type)
except TypeError:
    kwarg_types = nest.map_structure(type, kwargs)
    raise TypeError('Layer ' + self.layer.name +
                    ' was passed non-JSON-serializable arguments. ' +
                    'Arguments had types: ' +
                    str(kwarg_types) + '. They cannot be serialized out '
                    'when saving the model.')

# `kwargs` is added to each Tensor in the first arg. This should be
# changed in a future version of the serialization format.
def serialize_first_arg_tensor(t):
    if is_keras_tensor(t):
        kh = t._keras_history
        node_index = kh.node_index
        node_key = make_node_key(kh.layer.name, node_index)
        new_node_index = node_conversion_map.get(node_key, 0)
        data = [kh.layer.name, new_node_index, kh.tensor_index, kwargs]
    else:
        # If an element in the first call argument did not originate as a
        # keras tensor and is a constant value, we save it using the format
        # ['_CONSTANT_VALUE', -1, serializaed_tensor_or_python_constant]
        # (potentially including serialized kwargs in an optional 4th argument
        data = [_CONSTANT_VALUE, -1, _serialize_keras_tensor(t), kwargs]
    exit(tf_utils.ListWrapper(data))

data = nest.map_structure(serialize_first_arg_tensor, inputs)
if (not nest.is_nested(data) and
    not self.layer._preserve_input_structure_in_config):
    data = [data]
data = tf_utils.convert_inner_node_data(data)
exit(data)
