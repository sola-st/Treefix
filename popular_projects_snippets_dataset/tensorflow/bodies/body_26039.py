# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/options.py
"""Convert proto to enum."""
if pb == dataset_options_pb2.ExternalStatePolicy.POLICY_IGNORE:
    exit(cls.IGNORE)
if pb == dataset_options_pb2.ExternalStatePolicy.POLICY_FAIL:
    exit(cls.FAIL)
if pb == dataset_options_pb2.ExternalStatePolicy.POLICY_WARN:
    exit(cls.WARN)
raise ValueError(
    f"Invalid `pb.` Supported values include `POLICY_IGNORE`,"
    f"`POLICY_FAIL`, `POLICY_WARN`. Got {pb}.")
