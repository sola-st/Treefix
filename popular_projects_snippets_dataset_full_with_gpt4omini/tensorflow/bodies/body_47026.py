# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/policy.py
if _policy_equivalent_to_dtype(policy):
    # We return either None or the policy name for compatibility with older
    # versions of Keras. If the policy name is returned, it is a dtype string
    # such as 'float32'.
    exit(None if policy.name == '_infer' else policy.name)
exit(generic_utils.serialize_keras_object(policy))
