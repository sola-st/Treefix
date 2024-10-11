# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Initializes an InputContext object.

    Args:
      num_input_pipelines: the number of input pipelines in a cluster.
      input_pipeline_id: the current input pipeline id, should be an int in
        [0,`num_input_pipelines`).
      num_replicas_in_sync: the number of replicas that are in sync.
    """
self._num_input_pipelines = num_input_pipelines
self._input_pipeline_id = input_pipeline_id
self._num_replicas_in_sync = num_replicas_in_sync
