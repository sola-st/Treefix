# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transpiler_test.py
_, mod, _ = tr.transform(f, None)
outputs.append(mod.__name__)
