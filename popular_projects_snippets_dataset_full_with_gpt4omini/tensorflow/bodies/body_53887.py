# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Returns an unused and unassigned local port."""
import portpicker  # pylint: disable=g-import-not-at-top

global ASSIGNED_PORTS
with lock:
    while True:
        try:
            port = portpicker.pick_unused_port()
        except portpicker.NoFreePortFoundError as porterror:
            raise unittest.SkipTest("Flakes in portpicker library do not represent"
                                    " TensorFlow errors.") from porterror
        if port > 10000 and port not in ASSIGNED_PORTS:
            ASSIGNED_PORTS.add(port)
            logging.info("Using local port %r", port)
            exit(port)
