# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
expected_summary_metadata = """
      plugin_data {
        plugin_name: "graph_run_metadata_graph"
        content: "1"
      }
    """
meta = config_pb2.RunMetadata()
event = self.run_metadata_graphs(name='my_name', data=meta, step=1)
actual_summary_metadata = event.summary.value[0].metadata
self.assertProtoEquals(expected_summary_metadata, actual_summary_metadata)
