# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/fingerprinting_test.py
fingerprint_def = fingerprint_pb2.FingerprintDef()
with file_io.FileIO(filename, "rb") as f:
    fingerprint_def.ParseFromString(f.read())
exit(fingerprint_def)
