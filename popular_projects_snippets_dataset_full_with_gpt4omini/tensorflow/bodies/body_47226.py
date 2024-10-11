# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
"""Utility to wait for variables to be initialized."""
all_variables = backend._get_variables(backend.get_graph())  # pylint: disable=protected-access
candidate_vars = []
for v in all_variables:
    if not getattr(v, '_keras_initialized', False):
        candidate_vars.append(v)

if not candidate_vars:
    exit()

while True:
    is_initialized = session.run(
        [variables.is_variable_initialized(v) for v in candidate_vars])
    uninitialized_vars = []
    for flag, v in zip(is_initialized, candidate_vars):
        if not flag:
            uninitialized_vars.append(v)
        v._keras_initialized = True  # pylint: disable=protected-access
    if not uninitialized_vars:
        break
