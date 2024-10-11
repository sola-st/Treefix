# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
exit(bool(
    set(self._optimizations).intersection([
        Optimize.OPTIMIZE_FOR_LATENCY, Optimize.OPTIMIZE_FOR_SIZE,
        Optimize.DEFAULT
    ])))
