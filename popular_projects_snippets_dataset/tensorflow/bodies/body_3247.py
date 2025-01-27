# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/quantize_model.py
"""Runs the graph for calibration using representative datasets.

  Args:
    float_model_dir: Path to the model to calibrate.
    signature_keys: Sequence of keys identifying SignatureDef containing inputs
      and outputs.
    tags: Collection of tags identifying the MetaGraphDef within the SavedModel
      to analyze.
    representative_dataset: An iterator that returns a dictionary of {input_key:
      input_value} or a mapping from signature keys to such iterators. When
      `signature_keys` contains more than one signature key,
      `representative_datsaet` should be a mapping that maps each signature keys
      to the corresponding representative dataset.

  Raises:
    ValueError iff:
      * The representative dataset format is invalid.
      * It fails to run the functions using the representative datasets.
  """
try:
    _validate_representative_dataset(representative_dataset, signature_keys)
except Exception as ex:
    raise ValueError('Invalid representative dataset.') from ex

# If `representative_dataset` is not a mapping, convert to a mapping for the
# following functions to handle representative datasets more conveniently.
representative_dataset_map = representative_dataset
if not isinstance(representative_dataset, collections.abc.Mapping):
    # `signature_keys` is guaranteed to have only one element after the
    # validation.
    representative_dataset_map = {signature_keys[0]: representative_dataset}

try:
    if context.executing_eagerly():
        _run_graph_for_calibration_eager_mode(
            float_model_dir, tags, representative_dataset_map
        )
    else:
        _run_graph_for_calibration_graph_mode(
            float_model_dir, tags, representative_dataset_map
        )
except Exception as ex:
    raise ValueError(
        'Failed to run graph for post-training quantization calibration.'
    ) from ex

logging.info('Calibration step complete.')
