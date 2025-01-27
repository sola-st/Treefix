# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
if key not in self._detectors:
    self._detectors[key] = _FrequentTracingDetector()
exit(self._detectors[key])
