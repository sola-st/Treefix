# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
exit(control_flow_ops.group(
    variables.global_variables_initializer(),
    resources.initialize_resources(resources.shared_resources()),
    ops.get_collection('saved_model_initializers')))
