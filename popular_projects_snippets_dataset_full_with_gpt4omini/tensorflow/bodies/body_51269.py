# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/pywrap_saved_model_fingerprinting_test.py
export_dir = test.test_src_dir_path(
    "cc/saved_model/testdata/VarsAndArithmeticObjectGraph")
with file_io.FileIO(os.path.join(export_dir, "saved_model.pb"), "rb") as f:
    file_content = f.read()

fingerprint_def = fingerprint_pb2.FingerprintDef()
fingerprint_def.ParseFromString(
    fingerprinting.CreateFingerprintDef(file_content, export_dir))
# We cannot check the value of the saved_model_checksum due to
# non-determinism in serialization.
self.assertGreater(fingerprint_def.saved_model_checksum, 0)
self.assertEqual(fingerprint_def.graph_def_program_hash,
                 10127142238652115842)
self.assertEqual(fingerprint_def.signature_def_hash, 5693392539583495303)
self.assertEqual(fingerprint_def.saved_object_graph_hash,
                 3678101440349108924)
# TODO(b/242348400): The checkpoint hash is non-deterministic, so we cannot
# check its value here.
self.assertGreater(fingerprint_def.checkpoint_hash, 0)
