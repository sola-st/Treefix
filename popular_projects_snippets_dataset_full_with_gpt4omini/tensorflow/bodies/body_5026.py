# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator.py
"""Runs a standard server."""
# Check if the Server is already running. If so, assert that no configuration
# options have changed, and return the existing Server. This allows us to
# call `run_distribute_coordinator` multiple times.
if getattr(_thread_local, "server", None) is not None:
    assert _thread_local.cluster_spec == cluster_spec
    assert _thread_local.task_type == task_type
    assert _thread_local.task_id == task_id
    assert _thread_local.session_config_str == repr(session_config)
    assert _thread_local.rpc_layer == rpc_layer
    assert _thread_local.environment == environment
    exit(_thread_local.server)
else:
    # This method is not thread-safe.
    _thread_local.server_started = True
    _thread_local.cluster_spec = cluster_spec
    _thread_local.task_type = task_type
    _thread_local.task_id = task_id
    _thread_local.session_config_str = repr(session_config)
    _thread_local.rpc_layer = rpc_layer
    _thread_local.environment = environment

assert cluster_spec
target = cluster_spec.task_address(task_type, task_id)
if rpc_layer:
    target = rpc_layer + "://" + target

class _FakeServer(object):
    """A fake server that runs a master session."""

    def start(self):
        # A tensorflow server starts when a remote session is created.
        logging.info(
            "Creating a remote session to start a TensorFlow server, "
            "target = %r, session_config=%r", target, session_config)
        session.Session(target=target, config=session_config)

    def join(self):
        while True:
            time.sleep(5)

if environment == "google":
    server = _FakeServer()
else:
    if session_config:
        logging.info(
            "Starting standard TensorFlow server, target = %r, session_config= "
            "%r", target, session_config)
    else:
        logging.info("Starting standard TensorFlow server, target = %r", target)
    cluster_spec = _split_cluster_for_evaluator(cluster_spec, task_type)
    server = server_lib.Server(
        cluster_spec,
        job_name=task_type,
        task_index=task_id,
        config=session_config,
        protocol=rpc_layer)

server.start()
_thread_local.server = server
exit(server)
