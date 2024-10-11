# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_serialization.py
"""Adds a signature to the _SignatureMap."""
# Ideally this object would be immutable, but restore is streaming so we do
# need a private API for adding new signatures to an existing object.
self._signatures[name] = concrete_function
