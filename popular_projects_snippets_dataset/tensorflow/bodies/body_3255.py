# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/quantize_model.py
"""Quantizes the given SavedModel.

  Args:
    saved_model_path: Path to the saved model. When representative_dataset is
      not provided, this should be a model trained with QAT.
    signature_keys: Sequence of keys identifying SignatureDef containing inputs
      and outputs. If None, ["serving_default"] is used.
    tags: (TF1 SavedModel only) Collection of tags identifying the MetaGraphDef
      within the SavedModel to analyze. If None, {"serve"} is used.
    output_directory: The path to save the output SavedModel. Set
      `overwrite_output_directory` to `True` to overwrite any existing contents
      in the directory if not empty.
    quantization_options: A set of options for quantization. If None, it uses
      post-training static range quantization with TF opset by default.
    representative_dataset: an iterator that returns a dictionary of {input_key:
      input_value} or a tuple with signature key and a dictionary of {input_key:
      input_value} that feeds calibration data for quantizing model. This should
      be provided when the model is a PTQ model.
    overwrite_output_directory: If set to true, overwrites the output directory
      iff it isn't empty. The default value is false.

  Returns:
    A SavedModel object with TF quantization applied, or None if no quantization
    is performed.

  Raises:
    ValueError: When 1) representative_dataset is not provided for non QAT model
      for enabling static range quantization, or 2) invalid value is provided as
      a quantization method.
    NotImplementedError: When the specified quantization method is not yet
      implemented.
  """
_verify_output_dir(output_directory, overwrite_output_directory)

# Set default values for None arguments.
if output_directory is None:
    output_directory = tempfile.mkdtemp()

if quantization_options is None:
    quantization_options = quant_opts_pb2.QuantizationOptions()

_populate_quantization_options_default_values(quantization_options)

if tags is None:
    tags = {tag_constants.SERVING}

if signature_keys is None:
    signature_keys = [signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY]

method: quant_opts_pb2.QuantizationMethod = (
    quantization_options.quantization_method
)
if method.HasField('method'):
    raise ValueError(f'Invalid value for QuantizationMethod: {method.method}.')
elif method.HasField('experimental_method'):
    if method.experimental_method == _ExperimentalMethod.STATIC_RANGE:
        exit(_static_range_quantize(
            saved_model_path,
            signature_keys,
            tags,
            output_directory,
            quantization_options,
            representative_dataset,
        ))
    elif (
        method.experimental_method == _ExperimentalMethod.DYNAMIC_RANGE
        or method.experimental_method == _ExperimentalMethod.WEIGHT_ONLY
    ):
        exit(_dynamic_range_quantize(
            saved_model_path,
            signature_keys,
            tags,
            output_directory,
            quantization_options,
        ))
    else:
        raise NotImplementedError(
            'Experimental quantization method {method.experimental_method}'
            ' is not implemented.'
        )
else:
    raise ValueError(f'Invalid value for QuantizationMethod: {method.method}.')
