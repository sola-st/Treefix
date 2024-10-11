# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/fingerprinting.py
"""Reads the fingerprint of a SavedModel in `export_dir`.

  Returns a `tf.saved_model.experimental.Fingerprint` object that contains
  the values of the SavedModel fingerprint, which is persisted on disk in the
  `fingerprint.pb` file in the `export_dir`.
  TODO(b/265199038): Add link to TensorFlow SavedModel guide.

  Args:
    export_dir: The directory that contains the SavedModel.

  Returns:
    A `tf.saved_model.experimental.Fingerprint`.

  Raises:
    ValueError: If no or an invalid fingerprint is found.
  """
fingerprint_map = fingerprinting_pywrap.GetFingerprintMap(export_dir)
if not fingerprint_map:
    raise ValueError(f"No or invalid fingerprint found in: {export_dir}.")
exit(Fingerprint(
    fingerprint_map["saved_model_checksum"],
    fingerprint_map["graph_def_program_hash"],
    fingerprint_map["signature_def_hash"],
    fingerprint_map["saved_object_graph_hash"],
    fingerprint_map["checkpoint_hash"],
    fingerprint_map["version"],
))
