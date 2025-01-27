# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Create the Distributed Strategy session."""
session_config = get_default_session_config()

# If a session already exists, merge in its config; in the case there is a
# conflict, take values of the existing config.
global _SESSION
if getattr(_SESSION, 'session', None) and _SESSION.session._config:
    session_config.MergeFrom(_SESSION.session._config)

if is_tpu_strategy(distribution_strategy):
    # TODO(priyag, yuefengz): Remove this workaround when Distribute
    # Coordinator is integrated with keras and we can create a session from
    # there.
    distribution_strategy.configure(session_config)
    master = distribution_strategy.extended._tpu_cluster_resolver.master()  # pylint: disable=protected-access
    session = session_module.Session(config=session_config, target=master)
else:
    worker_context = dc.get_current_worker_context()
    if worker_context:
        dc_session_config = worker_context.session_config
        # Merge the default session config to the one from distribute
        # coordinator, which is fine for now since they don't have
        # conflicting configurations.
        dc_session_config.MergeFrom(session_config)
        session = session_module.Session(
            config=dc_session_config, target=worker_context.master_target)
    else:
        distribution_strategy.configure(session_config)
        session = session_module.Session(config=session_config)

set_session(session)
