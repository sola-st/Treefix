# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework.py
"""Constructor for `OnRunEndRequest`.

    Args:
      performed_action: (`OnRunStartAction`) Actually-performed action by the
        debug-wrapper session.
      run_metadata: run_metadata output from the run() call (if any).
      client_graph_def: (GraphDef) GraphDef from the client side, i.e., from
        the python front end of TensorFlow. Can be obtained with
        session.graph.as_graph_def().
      tf_error: (errors.OpError subtypes) TensorFlow OpError that occurred
        during the run (if any).
    """

_check_type(performed_action, str)
self.performed_action = performed_action

if run_metadata is not None:
    _check_type(run_metadata, config_pb2.RunMetadata)
self.run_metadata = run_metadata
self.client_graph_def = client_graph_def
self.tf_error = tf_error
