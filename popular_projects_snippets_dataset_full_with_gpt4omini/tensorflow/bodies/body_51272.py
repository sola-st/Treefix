# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/pywrap_saved_model_fingerprinting_test.py
export_dir = test.test_src_dir_path(
    "cc/saved_model/testdata/VarsAndArithmeticObjectGraph"
)
fingerprint_map = fingerprinting.GetFingerprintMap(export_dir)

fingerprint_def = fingerprint_pb2.FingerprintDef()
with file_io.FileIO(os.path.join(export_dir, "fingerprint.pb"), "rb") as f:
    fingerprint_def.ParseFromString(f.read())

self.assertEqual(
    fingerprint_map["saved_model_checksum"],
    fingerprint_def.saved_model_checksum,
)
self.assertEqual(
    fingerprint_map["graph_def_program_hash"],
    fingerprint_def.graph_def_program_hash,
)
self.assertEqual(
    fingerprint_map["signature_def_hash"],
    fingerprint_def.signature_def_hash,
)
self.assertEqual(
    fingerprint_map["saved_object_graph_hash"],
    fingerprint_def.saved_object_graph_hash,
)
self.assertEqual(
    fingerprint_map["checkpoint_hash"], fingerprint_def.checkpoint_hash
)
self.assertEqual(
    fingerprint_map["version"], fingerprint_def.version.producer
)
