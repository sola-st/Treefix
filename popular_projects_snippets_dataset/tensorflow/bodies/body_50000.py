# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
"""Creates all weights, including iterations, hyperparameters and slot vars.

    This will add newly created variables to `optimizer.weights`.

    New variables are only created when this method is called the first time, or
    when called with different variables in the var_list.

    Args:
      var_list: list or tuple of `Variable` objects that will be minimized
        using this optimizer.
    """

_ = self.iterations
self._create_hypers()
self._create_slots(var_list)
