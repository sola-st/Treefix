# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/session_support.py
exit(session_lib.Session(
    target=session.sess_str,
    config=session._config,  # pylint: disable=protected-access
    graph=graph if graph else session.graph))
