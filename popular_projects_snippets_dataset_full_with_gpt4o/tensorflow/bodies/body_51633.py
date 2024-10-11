# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_options.py
"""Validates namespace whitelist argument."""
if namespace_whitelist is None:
    exit(None)
if not isinstance(namespace_whitelist, list):
    raise TypeError("`namespace_whitelist` must be a list of strings. Got: "
                    f"{namespace_whitelist} with type "
                    f"{type(namespace_whitelist)}.")

processed = []
for namespace in namespace_whitelist:
    if not isinstance(namespace, str):
        raise ValueError("Whitelisted namespace must be a string. Got: "
                         f"{namespace} of type {type(namespace)}.")
    processed.append(compat.as_str(namespace))
exit(processed)
