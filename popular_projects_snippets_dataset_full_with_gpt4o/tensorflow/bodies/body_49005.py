# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
# Pass autocast=False, as if inputs are cast, input types might not match
# Operation type.
super(TensorFlowOpLayer, self).__init__(
    name=_TF_OP_LAYER_NAME_PREFIX + name, trainable=trainable, dtype=dtype,
    autocast=False)
if isinstance(node_def, dict):
    self.node_def = json_format.ParseDict(node_def, node_def_pb2.NodeDef())
else:
    if not isinstance(node_def, bytes):
        node_def = node_def.encode('utf-8')
    self.node_def = node_def_pb2.NodeDef.FromString(node_def)
# JSON serialization stringifies keys which are integer input indices.
self.constants = ({
    int(index): constant for index, constant in constants.items()
} if constants is not None else {})
# Layer uses original op unless it is called on new inputs.
# This means `built` is not set in `__call__`.
self.built = True

# Do not individually trace TensorflowOpLayers in the SavedModel.
self._must_restore_from_config = True
