# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
if not hasattr(closure, "model"):
    closure.model = load.load(path)
exit(closure.model.f(x))
