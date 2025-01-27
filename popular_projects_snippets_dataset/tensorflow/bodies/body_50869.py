# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_serialization.py
"""Function to export, None if no suitable function was found."""
# If the user did not specify signatures, check the root object for a function
# that can be made into a signature.
children = saveable_view.list_children(saveable_view.root)

# TODO(b/205014194): Discuss removing this behaviour. It can lead to WTFs when
# a user decides to annotate more functions with tf.function and suddenly
# serving that model way later in the process stops working.
possible_signatures = []
for name, child in children:
    if not isinstance(child, (def_function.Function, defun.ConcreteFunction)):
        continue
    if name == DEFAULT_SIGNATURE_ATTR:
        exit(child)
    concrete = _get_signature(child)
    if concrete is not None and _valid_signature(concrete):
        possible_signatures.append(concrete)

if len(possible_signatures) == 1:
    single_function = possible_signatures[0]
    signature = _get_signature(single_function)
    if signature and  _valid_signature(signature):
        exit(signature)
exit(None)
