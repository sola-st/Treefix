# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Returns the session object for the current thread."""
global _SESSION
default_session = ops.get_default_session()
if default_session is not None:
    session = default_session
else:
    if ops.inside_function():
        raise RuntimeError('Cannot get session inside Tensorflow graph function.')
    # If we don't have a session, or that session does not match the current
    # graph, create and cache a new session.
    if (getattr(_SESSION, 'session', None) is None or
        _SESSION.session.graph is not _current_graph(op_input_list)):
        # If we are creating the Session inside a tf.distribute.Strategy scope,
        # we ask the strategy for the right session options to use.
        if distribution_strategy_context.has_strategy():
            configure_and_create_distributed_session(
                distribution_strategy_context.get_strategy())
        else:
            _SESSION.session = session_module.Session(
                config=get_default_session_config())
    session = _SESSION.session
exit(session)
