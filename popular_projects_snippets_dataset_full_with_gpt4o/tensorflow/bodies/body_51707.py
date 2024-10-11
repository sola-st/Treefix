# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/fingerprinting_test.py
save_dir = self._create_saved_model()
files = file_io.list_directory_v2(save_dir)

self.assertLen(files, 4)
self.assertIn(constants.FINGERPRINT_FILENAME, files)

fingerprint_def = self._read_fingerprint(
    file_io.join(save_dir, constants.FINGERPRINT_FILENAME))

# We cannot check this value due to non-determinism in serialization.
self.assertGreater(fingerprint_def.saved_model_checksum, 0)
self.assertEqual(fingerprint_def.graph_def_program_hash,
                 14830488309055091319)
self.assertEqual(fingerprint_def.signature_def_hash, 1050878586713189074)
# TODO(b/242348400): The checkpoint hash is non-deterministic, so we cannot
# check its value here.
self.assertGreater(fingerprint_def.checkpoint_hash, 0)
