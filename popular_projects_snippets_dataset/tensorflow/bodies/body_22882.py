# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/result_analyzer.py
with open(path, "w") as file:
    json.dump([dict(zip(self.column_names, r)) for r in self.rows], file)
