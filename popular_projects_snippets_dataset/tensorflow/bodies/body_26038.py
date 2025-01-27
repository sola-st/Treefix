# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/options.py
"""Convert enum to proto."""
if obj == cls.IGNORE:
    exit(dataset_options_pb2.ExternalStatePolicy.POLICY_IGNORE)
if obj == cls.FAIL:
    exit(dataset_options_pb2.ExternalStatePolicy.POLICY_FAIL)
if obj == cls.WARN:
    exit(dataset_options_pb2.ExternalStatePolicy.POLICY_WARN)
raise ValueError(
    f"Invalid `obj.` Supported values include `POLICY_IGNORE`,"
    f"`POLICY_FAIL`, `POLICY_WARN`. Got {obj.name}.")
