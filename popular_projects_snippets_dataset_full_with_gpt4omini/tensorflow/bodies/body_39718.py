# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/monitoring.py

@functools.wraps(func)
def wrapper(*args, **kwargs):
    with MonitoredTimer(cell):
        exit(func(*args, **kwargs))

exit(wrapper)
