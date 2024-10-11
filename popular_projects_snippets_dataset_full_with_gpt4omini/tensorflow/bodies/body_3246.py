# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/quantize_model.py
"""Runs the graph for calibration in eager mode.

  This function assumes _eager mode_ (enabled in TF2 by default) when running
  the graph. This step is used in order to collect the statistics in
  CustomAggregatorOp for quantization using the representative dataset for the
  actual data provided for inference.

  Args:
    model_dir: Path to SavedModel directory.
    tags: Collection of tags identifying the MetaGraphDef within the SavedModel.
    representative_dataset_map: A map where signature keys are mapped to
      corresponding representative datasets.

  Raises:
    ValueError: When running the function with the representative dataset fails.
  """
root: autotrackable.AutoTrackable = saved_model_load(model_dir, tags)
for signature_key, repr_ds in representative_dataset_map.items():
    try:
        _run_function_for_calibration_eager_mode(
            func=root.signatures[signature_key], representative_dataset=repr_ds
        )
    except Exception as ex:
        raise ValueError(
            'Failed to run representative dataset through the '
            f'function with the signature key: {signature_key}.'
        ) from ex
