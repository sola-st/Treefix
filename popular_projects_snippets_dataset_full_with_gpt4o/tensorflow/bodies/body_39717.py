# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/monitoring.py
with MonitoredTimer(cell):
    exit(func(*args, **kwargs))
