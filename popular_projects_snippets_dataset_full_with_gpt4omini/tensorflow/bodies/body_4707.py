# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
input_context = distribute_lib.InputContext(
    num_input_pipelines=1, input_pipeline_id=0, num_replicas_in_sync=42)
self.assertEqual(
    "tf.distribute.InputContext(input pipeline id 0, total: 1)",
    str(input_context))
input_context = distribute_lib.InputContext(
    num_input_pipelines=3, input_pipeline_id=1, num_replicas_in_sync=42)
self.assertEqual(
    "tf.distribute.InputContext(input pipeline id 1, total: 3)",
    str(input_context))
