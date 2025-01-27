# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/fingerprinting.py
"""Initializes the instance based on values in the SavedModel fingerprint.

    Args:
      saved_model_checksum: Value of the`saved_model_checksum`.
      graph_def_program_hash: Value of the `graph_def_program_hash`.
      signature_def_hash: Value of the `signature_def_hash`.
      saved_object_graph_hash: Value of the `saved_object_graph_hash`.
      checkpoint_hash: Value of the `checkpoint_hash`.
      version: Value of the producer field of the VersionDef.
    """
self.saved_model_checksum = saved_model_checksum
self.graph_def_program_hash = graph_def_program_hash
self.signature_def_hash = signature_def_hash
self.saved_object_graph_hash = saved_object_graph_hash
self.checkpoint_hash = checkpoint_hash
self.version = version
