# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
"""Returns a list of `tf.Variable`s.

      The list contains `number_replicas` `tf.Variable`s and can be used to
      initialize a `TPUMirroredVariable`.

      Args:
        **kwargs: the keyword arguments for creating a variable
      """
initial_value = None
value_list = []
for i, d in enumerate(devices):
    with ops.device(d):
        if i == 0:
            initial_value = kwargs["initial_value"]
            # Note: some v1 code expects variable initializer creation to happen
            # inside a init_scope.
            with maybe_init_scope():
                initial_value = initial_value() if callable(
                    initial_value) else initial_value

        if i > 0:
            # Give replicas meaningful distinct names:
            var0name = value_list[0].name.split(":")[0]
            # We append a / to variable names created on replicas with id > 0 to
            # ensure that we ignore the name scope and instead use the given
            # name as the absolute name of the variable.
            kwargs["name"] = "%s/replica_%d/" % (var0name, i)
        kwargs["initial_value"] = initial_value

        with context.device_policy(context.DEVICE_PLACEMENT_SILENT):
            v = next_creator(**kwargs)

        assert not isinstance(v, tpu_values.TPUMirroredVariable)
        value_list.append(v)
exit(value_list)
