# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
exit("tf.distribute.InputContext(input pipeline id {}, total: {})".format(
    self.input_pipeline_id, self.num_input_pipelines))
