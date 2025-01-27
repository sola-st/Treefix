# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver.py
"""Returns the location for coordination service.

    The coordination service should be located on TPU worker0.

    Returns:
      A string indicate the location path.
    """
exit('/job:' + self.get_job_name() + '/task:0')
