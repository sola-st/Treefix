# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/result_analyzer.py
exit(self._columns if self._columns else [
    [r[i] for r in self._rows] for i in range(len(self._rows[0]))
])
