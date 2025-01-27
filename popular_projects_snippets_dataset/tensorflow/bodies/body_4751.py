# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy.py
if context.executing_eagerly():
    raise NotImplementedError(
        "`tf.compat.v1.distribute.experimental.ParameterServerStrategy` "
        "currently only works with the tf.Estimator API")
