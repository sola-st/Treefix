# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/quantize_model.py
"""Quantizes the given SavedModel via static range quantization.

  If the model is not trained with Quantization-Aware Training (QAT) technique,
  it requires `representative_dataset` to collect statistics required for
  quantization. If non-None `representative_dataset` is provided with a QAT
  model input, `representative_dataset` will be ignored.

  Args:
    saved_model_path: Path to the saved model. When representative_dataset is
      not provided, this should be a model trained with QAT.
    signature_keys: Sequence of keys identifying SignatureDef containing inputs
      and outputs.
    tags: Collection of tags identifying the MetaGraphDef within the SavedModel
      to analyze.
    output_directory: The path to save the output SavedModel. The directory will
      be overwritten if not empty.
    quantization_options: QuantizationOptions proto describing quantization
      related config.
    representative_dataset: a generator that returns a dictionary in {input_key:
      input_value} format or a tuple with signature key and a dictionary in
      {input_key: input_value} format that feeds calibration data for quantizing
      model. This should be provided when the model is not a QAT model.

  Returns:
    A SavedModel object with TF quantization applied.

  Raises:
    ValueError: when representative_dataset is not provided for non-QAT model.
    RuntimeError: When a MetaGraphDef could not be found associated with `tags`
      in the SavedModel.
  """
logging.info(
    'Running static range quantization on model: %s', saved_model_path
)
logging.info('Using SignatureDef keys: %s', signature_keys)
logging.info('Using tags: %s', tags)
logging.info('QuantizationOptions: \n%s', quantization_options)

is_qat_saved_model = _is_qat_saved_model(saved_model_path)
signature_def_map = save_model.get_signatures_from_saved_model(
    saved_model_path, signature_keys, tags
)

# Checks if the model is from QAT
if representative_dataset is None and not is_qat_saved_model:
    raise ValueError(
        'When `representative_dataset` is not provided, the model should be '
        'trained with quantization-aware training (QAT).'
    )
if quantization_options.min_num_elements_for_weights > 0:
    logging.warn(
        'min_num_elements_for_weights is set but is not supported for the '
        'Post-training static range quantization. '
        'The flag is ignored.'
    )

if is_qat_saved_model:
    exported_model = _run_static_range_qat(
        saved_model_path, signature_keys, tags, quantization_options
    )
else:
    exported_model, signature_def_map = _run_static_range_ptq(
        saved_model_path,
        signature_keys,
        tags,
        quantization_options,
        representative_dataset,
        signature_def_map,
    )

save_model.save_model_v1(
    exported_model.graph_def,
    output_directory,
    signature_def_map,
    tags,
    init_op_name=exported_model.init_node_name,
    restore_op_name=exported_model.restore_node_name,
    checkpoint_dir=exported_model.checkpoint_dir,
    variable_shared_names=exported_model.variable_shared_names,
)

exit(saved_model_load(output_directory))
