# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/quantize_model.py
"""Runs static-range Post-Training Quantization.

  Runs static-range PTQ for the model. Runs the calibration step with
  `representative_dataset` to collect statistics required for quantization. This
  produces the quantized GraphDef along with the SignatureDefs which might have
  been modified according to the changes in the graph.

  Args:
    saved_model_path: Path to SavedModel.
    signature_def_keys: Keys of the signature defs of the functions that are the
      target for quantization.
    tags: Tags to identify the MetaGraphDef to be used for quantization.
    quant_opts: Quantization options.
    representative_dataset: Representative dataset used for the calibration
      step. Representative datasets should exist for each signature def key in
      `signature_def_keys`.
    signature_def_map: Signature def key -> SignatureDef mapping.

  Raises:
    ValueError if the graph doesn't contain a valid signature.

  Returns:
    exported_model: Contains the GraphDef and extra metadata required for saving
      the quantized graph to SavedModel.
    signature_def_map: Contains the SignatureDefs, possibly modified
      according to the quantized graph to match the original signature defs.
  """
logging.info('Running post-training quantization pre-calibration step.')
exported_model_serialized = (
    quantize_model_wrapper.quantize_ptq_model_pre_calibration(
        saved_model_path,
        list(signature_def_keys),
        set(tags),
        quant_opts.SerializeToString(),
    )
)

exported_model = exported_model_pb2.ExportedModel.FromString(
    exported_model_serialized
)

graph_def = exported_model.graph_def
for function_def in graph_def.library.function:
    for node_def in function_def.node_def:
        if node_def.op == 'CustomAggregator':
            node_def.attr['id'].s = uuid.uuid4().hex.encode('ascii')

float_model_dir = tempfile.mkdtemp()
save_model.save_model_v1(
    graph_def,
    float_model_dir,
    signature_def_map,
    tags,
    exported_model.init_node_name,
    exported_model.restore_node_name,
    exported_model.checkpoint_dir,
    exported_model.variable_shared_names,
)

# Uses the representative dataset to collect statistics for calibration.
# Handles the graph mode execution separately in case TF2 is disabled or
# eager execution is disabled. The min & max values are stored separately
# in a global CalibratorSingleton instance.
_run_graph_for_calibration(
    float_model_dir, signature_def_keys, tags, representative_dataset
)
_add_calibration_statistics(graph_def)

calibrated_model_dir = tempfile.mkdtemp()
save_model.save_model_v1(
    graph_def,
    calibrated_model_dir,
    signature_def_map,
    tags,
    exported_model.init_node_name,
    exported_model.restore_node_name,
    exported_model.checkpoint_dir,
    exported_model.variable_shared_names,
)

logging.info('Running post-training quantization post-calibration step.')
exported_model_serialized = (
    quantize_model_wrapper.quantize_ptq_model_post_calibration(
        calibrated_model_dir,
        list(signature_def_keys),
        set(tags),
        quant_opts.SerializeToString(),
    )
)

exported_model = exported_model_pb2.ExportedModel.FromString(
    exported_model_serialized
)

exit((exported_model,
    signature_def_map,))
