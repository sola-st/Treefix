# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/quantize_model.py
"""Replaces tf.Tensors by their evaluated numpy arrays.

  This assumes that tf.Tensors in representative samples are created in the
  default Graph. It will raise an error if tensors are created in a different
  graph.

  Args:
    repr_ds_map: SignatureDef key -> RepresentativeDataset mapping.
  """
with session.Session() as sess:
    for signature_def_key in repr_ds_map:
        # Replaces the dataset with a new dataset where tf.Tensors are replaced
        # by their evaluated values.
        ds = repr_ds_map[signature_def_key]
        repr_ds_map[signature_def_key] = (
            repr_dataset.replace_tensors_by_numpy_ndarrays(ds, sess)
        )
