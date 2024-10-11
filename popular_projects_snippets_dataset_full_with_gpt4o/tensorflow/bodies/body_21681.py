# Extracted from ./data/repos/tensorflow/tensorflow/python/training/coordinator_test.py
try:
    wait_for_stop.wait()
    raise ex
except RuntimeError as e:
    if report_exception:
        coord.request_stop(e)
    else:
        coord.request_stop(sys.exc_info())
finally:
    if set_when_stopped:
        set_when_stopped.set()
