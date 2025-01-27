# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v1.py
"""Returns gradients of `loss` with respect to `params`.

    Args:
        loss: Loss tensor.
        params: List of variables.

    Returns:
        List of gradient tensors.

    Raises:
        ValueError: In case any gradient cannot be computed (e.g. if gradient
          function not implemented).
    """
grads = backend.gradients(loss, params)
if any(g is None for g in grads):
    raise ValueError('An operation has `None` for gradient. '
                     'Please make sure that all of your ops have a '
                     'gradient defined (i.e. are differentiable). '
                     'Common ops without gradient: '
                     'backend.argmax, backend.round, backend.eval.')
if hasattr(self, 'clipnorm'):
    grads = [clip_ops.clip_by_norm(g, self.clipnorm) for g in grads]
if hasattr(self, 'clipvalue'):
    grads = [
        clip_ops.clip_by_value(g, -self.clipvalue, self.clipvalue)
        for g in grads
    ]
exit(grads)
