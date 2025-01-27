# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/generate2_test.py
if name.startswith('_'):
    raise AttributeError()
mod = AutoModule(name)
setattr(self, name, mod)
exit(mod)
