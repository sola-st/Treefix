# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/quantize_model.py
"""Quantizes the given SavedModel via post-training dynamic range quantization.

  Weight-only quantization also uses this path.

  Args:
    saved_model_path: Path to the saved model.
    signature_keys: Sequence of keys identifying SignatureDef containing inputs
      and outputs.
    tags: Collection of tags identifying the MetaGraphDef within the SavedModel
      to analyze.
    output_directory: The path to save the output SavedModel. The directory will
      be overwritten if not empty.
    quantization_options: QuantizationOptions proto describing quantization
      related config.

  Returns:
    A SavedModel object with TF quantization applied.

  Raises:
    ValueError: when the model is QAT model.
  """
if (
    quantization_options.quantization_method.experimental_method
    == _ExperimentalMethod.WEIGHT_ONLY
):
    mode_str = 'weight-only quantization'
else:
    mode_str = 'dynamic-range quantization'
if _is_qat_saved_model(saved_model_path):
    raise ValueError(
        'The models trained with quantization-aware training (QAT) is not '
        'supported for %s.' % mode_str
    )

logging.info(
    'Running post-training %s on model: %s', mode_str, saved_model_path
)
logging.info('Using SignatureDef keys: %s', signature_keys)
logging.info('Using tags: %s', tags)
logging.info('QuantizationOptions: \n%s', quantization_options)

# Check default quantization option values for post-training dynamic range
# quantization case.
# TODO(b/242805842): Find good minimum_elements_for_weights number for server.
# please also update default value in tflite converter:
# tensorflow/compiler/mlir/lite/tf_to_tfl_flatbuffer.cc;l=201
if quantization_options.min_num_elements_for_weights == 0:
    (quantization_options.min_num_elements_for_weights) = (
        _DYNAMIC_RANGE_DEFAULT_MIN_NUM_ELEMENTS_FOR_WEIGHTS
    )
    logging.warn(
        (
            'QuantizationOptions.min_num_elements_for_weights is not set (0). '
            'Setting to the default value: %s.'
        ),
        _DYNAMIC_RANGE_DEFAULT_MIN_NUM_ELEMENTS_FOR_WEIGHTS,
    )

# Apply post-training dynamic range quantization to the model.
exported_model_serialized = quantize_model_wrapper.quantize_ptq_dynamic_range(
    saved_model_path,
    list(signature_keys),
    set(tags),
    quantization_options.SerializeToString(),
)

exported_model = exported_model_pb2.ExportedModel.FromString(
    exported_model_serialized
)
signature_def_map = save_model.get_signatures_from_saved_model(
    saved_model_path, signature_keys, tags
)

save_model.save_model_v1(
    exported_model.graph_def,
    output_directory,
    signature_def_map,
    tags=tags,
    init_op_name=exported_model.init_node_name,
)

exit(saved_model_load(output_directory))
