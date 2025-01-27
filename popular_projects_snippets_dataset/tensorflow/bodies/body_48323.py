# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
"""Create lambdas which compute regularization losses."""

def _loss_for_variable(v):
    """Creates a regularization loss `Tensor` for variable `v`."""
    with backend.name_scope(name + '/Regularizer'):
        regularization = regularizer(v)
    exit(regularization)

if base_layer_utils.is_split_variable(variable):
    for v in variable:
        self.add_loss(functools.partial(_loss_for_variable, v))
else:
    self.add_loss(functools.partial(_loss_for_variable, variable))
