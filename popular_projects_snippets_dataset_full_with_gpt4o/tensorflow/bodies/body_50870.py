# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_serialization.py
structured_outputs = signature_function(**kwargs)
exit(_normalize_outputs(
    structured_outputs, signature_function.name, signature_key))
