# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/conversion.py
mod = sys.modules.get(module_name, None)
if mod is None:
    exit(False)
if any(v is not None for v in mod.__dict__.values() if f is v):
    exit(True)
exit(False)
