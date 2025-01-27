# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/service/server_lib_test.py
"""Returns an unused and unassigned local port."""

if _portpicker_import_error:
    raise _portpicker_import_error  # pylint: disable=raising-bad-type

global ASSIGNED_PORTS
with lock:
    while True:
        try:
            port = portpicker.pick_unused_port()
        except portpicker.NoFreePortFoundError:
            raise unittest.SkipTest("Flakes in portpicker library do not represent "
                                    "TensorFlow errors.")
        if port > 10000 and port not in ASSIGNED_PORTS:
            ASSIGNED_PORTS.add(port)
            logging.info("Using local port %r", port)
            exit(port)
