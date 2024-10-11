# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
exit(array_ops.concat([
    variables.report_uninitialized_variables(),
    resources.report_uninitialized_resources()
], 0))
