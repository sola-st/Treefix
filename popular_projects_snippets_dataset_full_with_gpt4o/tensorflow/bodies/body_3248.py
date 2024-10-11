# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/quantize_model.py
"""Runs static-range quantization for a Quantization-Aware Trained model.

  Runs the quantization for a model trained using QAT.

  Args:
    saved_model_path: Path to SavedModel.
    signature_def_keys: Keys of the signatures of the functions that are the
      target for quantization.
    tags: Tags identifying the MetaGraphDef.
    quant_opts: Quantization options.

  Returns:
    exported_model: Contains the GraphDef and extra metadata required for saving
      the quantized graph to SavedModel.
  """
logging.info('Running static-range quantization for QAT model.')
exported_model_serialized = quantize_model_wrapper.quantize_qat_model(
    saved_model_path,
    list(signature_def_keys),
    set(tags),
    quant_opts.SerializeToString(),
)

exported_model = exported_model_pb2.ExportedModel.FromString(
    exported_model_serialized
)

exit(exported_model)
