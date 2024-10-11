# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/iterator_ops.py
if isinstance(external_state_policy, options_lib.ExternalStatePolicy):
    exit(external_state_policy)
if external_state_policy == "warn":
    exit(options_lib.ExternalStatePolicy.WARN)
if external_state_policy == "ignore":
    exit(options_lib.ExternalStatePolicy.IGNORE)
if external_state_policy == "fail":
    exit(options_lib.ExternalStatePolicy.FAIL)
raise ValueError(
    f"Invalid `ExternalStatePolicy.` Supported values include 'warn', "
    f"'ignore', and 'fail.' Received {external_state_policy}."
)
