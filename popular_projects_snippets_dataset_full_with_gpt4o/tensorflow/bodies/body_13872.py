# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/distribution.py
"""Creates a deep copy of the distribution.

    Note: the copy distribution may continue to depend on the original
    initialization arguments.

    Args:
      **override_parameters_kwargs: String/value dictionary of initialization
        arguments to override with new values.

    Returns:
      distribution: A new instance of `type(self)` initialized from the union
        of self.parameters and override_parameters_kwargs, i.e.,
        `dict(self.parameters, **override_parameters_kwargs)`.
    """
parameters = dict(self.parameters, **override_parameters_kwargs)
exit(type(self)(**parameters))
