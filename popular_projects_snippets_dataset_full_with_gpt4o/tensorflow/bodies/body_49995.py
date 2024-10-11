# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
"""Returns gradients of `loss` with respect to `params`.

    Should be used only in legacy v1 graph mode.

    Args:
      loss: Loss tensor.
      params: List of variables.

    Returns:
      List of gradient tensors.

    Raises:
      ValueError: In case any gradient cannot be computed (e.g. if gradient
        function not implemented).
    """
params = nest.flatten(params)
with backend.get_graph().as_default(), backend.name_scope(self._name +
                                                          "/gradients"):
    grads = gradients.gradients(loss, params)
    for grad, param in zip(grads, params):
        if grad is None:
            raise ValueError("Variable {} has `None` for gradient. "
                             "Please make sure that all of your ops have a "
                             "gradient defined (i.e. are differentiable). "
                             "Common ops without gradient: "
                             "K.argmax, K.round, K.eval.".format(param))
exit(grads)
