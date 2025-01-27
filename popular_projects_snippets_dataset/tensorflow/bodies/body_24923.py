# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data_test.py
dump_root = "/tmp/tfdbg_1"
debug_dump_rel_path = "ns1/ns2/node_foo_1_2_DebugIdentity_1472563253536385"
datum = debug_data.DebugTensorDatum(dump_root, debug_dump_rel_path)

self.assertIsNone(datum.dump_size_bytes)
