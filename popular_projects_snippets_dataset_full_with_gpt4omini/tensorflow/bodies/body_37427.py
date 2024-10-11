# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
expected_run_metadata = """
      step_stats {
        dev_stats {
          device: "cpu:0"
          node_stats {
            node_name: "hello"
          }
        }
      }
      function_graphs {
        pre_optimization_graph {
          node {
            name: "foo"
          }
        }
      }
    """
meta = self.create_run_metadata()
event = self.run_metadata(name='my_name', data=meta, step=1)
first_val = event.summary.value[0]

actual_run_metadata = config_pb2.RunMetadata.FromString(
    first_val.tensor.string_val[0])
self.assertProtoEquals(expected_run_metadata, actual_run_metadata)
