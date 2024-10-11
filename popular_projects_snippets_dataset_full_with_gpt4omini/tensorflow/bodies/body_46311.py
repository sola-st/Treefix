# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_fndefs.py
if init_from:
    self.value = set(init_from)
else:
    self.value = set()
