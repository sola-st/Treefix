# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
# pylint: disable=g-doc-return-or-yield,g-doc-args
"""DEPRECATED: use `update_config_proto` instead.

    Configures the strategy class.

    DEPRECATED: This method's functionality has been split into the strategy
    constructor and `update_config_proto`. In the future, we will allow passing
    cluster and config_proto to the constructor to configure the strategy. And
    `update_config_proto` can be used to update the config_proto based on the
    specific strategy.
    """
exit(self._extended._configure(  # pylint: disable=protected-access
    session_config, cluster_spec, task_type, task_id))
