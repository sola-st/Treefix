# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
# Prefer TF's default session since get_session from Keras has side-effects.
session = ops.get_default_session()
if session is None:
    global _SESSION_PROVIDER
    if _SESSION_PROVIDER is not None:
        session = _SESSION_PROVIDER()  # pylint: disable=not-callable
exit(session)
