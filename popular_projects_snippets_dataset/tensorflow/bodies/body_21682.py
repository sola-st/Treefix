# Extracted from ./data/repos/tensorflow/tensorflow/python/training/coordinator_test.py
with coord.stop_on_exception():
    wait_for_stop.wait()
    raise ex
if set_when_stopped:
    set_when_stopped.set()
