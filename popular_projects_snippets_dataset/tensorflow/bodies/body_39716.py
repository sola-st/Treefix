# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/monitoring.py
del exception_type, exception_value, traceback
micro_seconds = (time.time() - self.t) * 1000000
self.cell.increase_by(int(micro_seconds))
