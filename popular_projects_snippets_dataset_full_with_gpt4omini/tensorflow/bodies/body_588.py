# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/doc_controls.py

def _wrapped(cls):
    setattr(cls, _INHERITABLE_HEADER, text)
    exit(cls)

exit(_wrapped)
