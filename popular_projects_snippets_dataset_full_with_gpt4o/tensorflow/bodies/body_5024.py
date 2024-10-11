# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator.py
# A tensorflow server starts when a remote session is created.
logging.info(
    "Creating a remote session to start a TensorFlow server, "
    "target = %r, session_config=%r", target, session_config)
session.Session(target=target, config=session_config)
