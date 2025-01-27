# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/builder_impl.py
"""Validates the `SignatureDef` entries in the signature def map.

    Validation of entries in the signature def map includes ensuring that the
    `name` and `dtype` fields of the TensorInfo protos of the `inputs` and
    `outputs` of each `SignatureDef` are populated. Also ensures that reserved
    SignatureDef keys for the initialization and train ops are not used.

    Args:
      signature_def_map: The map of signature defs to be validated.

    Raises:
      AssertionError: If a TensorInfo is not valid.
      KeyError: If a reserved signature key is used in the map.
    """
for signature_def_key in signature_def_map:
    signature_def = signature_def_map[signature_def_key]
    inputs = signature_def.inputs
    outputs = signature_def.outputs
    for inputs_key in inputs:
        self._validate_tensor_info(inputs[inputs_key])
    for outputs_key in outputs:
        self._validate_tensor_info(outputs[outputs_key])
if constants.INIT_OP_SIGNATURE_KEY in signature_def_map:
    raise KeyError(
        f"SignatureDef map key \"{constants.INIT_OP_SIGNATURE_KEY}\" is "
        "reserved for initialization. Please use a different key.")
if constants.TRAIN_OP_SIGNATURE_KEY in signature_def_map:
    raise KeyError(
        f"SignatureDef map key \"{constants.TRAIN_OP_SIGNATURE_KEY}\" is "
        f"reserved for the train op. Please use a different key.")
