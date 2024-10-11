# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data_test.py
dump_root = "/tmp/tfdbg_1"
debug_dump_rel_path = (
    debug_data.METADATA_FILE_PREFIX + debug_data.DEVICE_TAG +
    ",job_localhost,replica_0,task_0,cpu_0" +
    "/ns1/ns2/node_a_1_2_DebugIdentity_1472563253536385")

datum = debug_data.DebugTensorDatum(dump_root, debug_dump_rel_path)

self.assertEqual("DebugIdentity", datum.debug_op)
self.assertEqual("ns1/ns2/node_a_1", datum.node_name)
self.assertEqual(2, datum.output_slot)
self.assertEqual("ns1/ns2/node_a_1:2", datum.tensor_name)
self.assertEqual(1472563253536385, datum.timestamp)
self.assertEqual("ns1/ns2/node_a_1:2:DebugIdentity", datum.watch_key)
self.assertEqual(
    os.path.join(dump_root, debug_dump_rel_path), datum.file_path)
self.assertEqual(
    "{DebugTensorDatum (/job:localhost/replica:0/task:0/cpu:0) "
    "%s:%d @ %s @ %d}" % (datum.node_name,
                          datum.output_slot,
                          datum.debug_op,
                          datum.timestamp), str(datum))
self.assertEqual(
    "{DebugTensorDatum (/job:localhost/replica:0/task:0/cpu:0) "
    "%s:%d @ %s @ %d}" % (datum.node_name,
                          datum.output_slot,
                          datum.debug_op,
                          datum.timestamp), repr(datum))
