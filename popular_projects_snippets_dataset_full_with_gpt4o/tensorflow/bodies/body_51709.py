# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/fingerprinting_test.py
save_dir = self._create_saved_model()
fingerprint = read_fingerprint(save_dir)

fingerprint_def = self._read_fingerprint(
    file_io.join(save_dir, constants.FINGERPRINT_FILENAME)
)

self.assertEqual(
    fingerprint.saved_model_checksum, fingerprint_def.saved_model_checksum
)
self.assertEqual(
    fingerprint.graph_def_program_hash,
    fingerprint_def.graph_def_program_hash,
)
self.assertEqual(
    fingerprint.signature_def_hash, fingerprint_def.signature_def_hash
)
self.assertEqual(
    fingerprint.saved_object_graph_hash,
    fingerprint_def.saved_object_graph_hash,
)
self.assertEqual(
    fingerprint.checkpoint_hash, fingerprint_def.checkpoint_hash
)
self.assertEqual(fingerprint.version, fingerprint_def.version.producer)
