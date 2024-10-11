# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
exit(array_ops.concat([
    variables.report_uninitialized_variables(
        variables.global_variables()),
    resources.report_uninitialized_resources(
        resources.shared_resources())
], 0))
