# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/quantize_model.py
"""Runs the graph for calibration in graph mode.

  This function assumes _graph mode_ (used when legacy TF1 is used or when eager
  mode is explicitly disabled) when running the graph. This step is used in
  order to collect the statistics in CustomAggregatorOp for quantization using
  the representative dataset for the actual data provided for inference.

  Args:
    model_dir: Path to SavedModel directory.
    tags: Collection of tags identifying the MetaGraphDef within the SavedModel.
    representative_dataset_map: A map where signature keys are mapped to
      corresponding representative datasets.

  Raises:
    ValueError: When running the function with the representative dataset fails.
  """
# Replace tf.Tensors by numpy ndarrays in order to reuse the samples in a
# different graph when running the calibration.
_replace_tensors_by_numpy_ndarrays(representative_dataset_map)

# Run the calibration in a new graph to avoid name collision, which could
# happen when the same model is loaded multiple times in the default graph.
with ops.Graph().as_default(), session.Session() as sess:
    meta_graph: meta_graph_pb2.MetaGraphDef = saved_model_loader.load(
        sess, tags, export_dir=model_dir
    )

    for signature_key, repr_ds in representative_dataset_map.items():
        sig_def = meta_graph.signature_def[signature_key]

        try:
            _run_function_for_calibration_graph_mode(
                sess, signature_def=sig_def, representative_dataset=repr_ds
            )
        except Exception as ex:
            raise ValueError(
                'Failed to run representative dataset through the '
                f'function with the signature key: {signature_key}.'
            ) from ex
