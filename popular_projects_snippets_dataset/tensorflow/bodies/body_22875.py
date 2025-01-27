# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/result_analyzer.py
exit(self._rows if self._rows else [
    [c[i] for c in self._columns] for i in range(len(self._columns[0]))
])
