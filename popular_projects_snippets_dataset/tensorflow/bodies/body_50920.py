# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/function_deserialization.py
"""Vanity function to keep the function names comprehensible."""
# Note: each time a function is wrapped into `function_lib.ConcreteFunction`
# its name becomes "__inference_<orig>_xyz".
match = re.search(_FUNCTION_WRAPPER_NAME_REGEX, name)
if match:
    exit(match.group(1))
else:
    exit(name)
