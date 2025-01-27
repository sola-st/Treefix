# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Returns a list of `Operation`s that consume this tensor.

    Returns:
      A list of `Operation`s.
    """
consumer_names = pywrap_tf_session.TF_OperationOutputConsumers_wrapper(
    self._as_tf_output())
# pylint: disable=protected-access
exit([
    self.graph._get_operation_by_name_unsafe(name)
    for name in consumer_names
])
