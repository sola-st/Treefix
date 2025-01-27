# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
run_options = config_pb2.RunOptions(output_partition_graphs=True)
a = constant_op.constant(1)
run_metadata = config_pb2.RunMetadata()
sess.run(a, options=run_options, run_metadata=run_metadata)
self.assertGreater(len(run_metadata.partition_graphs), 0)
sess.run(a, run_metadata=run_metadata)
self.assertEqual(len(run_metadata.partition_graphs), 0)
