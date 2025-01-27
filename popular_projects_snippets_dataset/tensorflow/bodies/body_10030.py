# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli.py
"""Function triggered by run command.

  Raises:
    AttributeError: An error when neither --inputs nor --input_exprs is passed
    to run command.
  """
if not _SMCLI_INPUTS.value and not _SMCLI_INPUT_EXPRS.value and not _SMCLI_INPUT_EXAMPLES.value:
    raise AttributeError(
        'At least one of --inputs, --input_exprs or --input_examples must be '
        'required')
tensor_key_feed_dict = load_inputs_from_input_arg_string(
    _SMCLI_INPUTS.value,
    _SMCLI_INPUT_EXPRS.value,
    _SMCLI_INPUT_EXAMPLES.value)
run_saved_model_with_feed_dict(
    _SMCLI_DIR.value,
    _SMCLI_TAG_SET.value,
    _SMCLI_SIGNATURE_DEF.value,
    tensor_key_feed_dict,
    _SMCLI_OUTDIR.value,
    _SMCLI_OVERWRITE.value,
    worker=_SMCLI_WORKER.value,
    init_tpu=_SMCLI_INIT_TPU.value,
    use_tfrt=_SMCLI_USE_TFRT.value,
    tf_debug=_SMCLI_TF_DEBUG.value)
