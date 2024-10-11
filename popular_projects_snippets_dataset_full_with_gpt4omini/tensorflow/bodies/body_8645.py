# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/estimator_training.py
"""Initializes RunConfig for distribution strategies."""
# pylint: disable=protected-access
if (config._experimental_distribute and
    config._experimental_distribute.train_distribute):
    if config._train_distribute:
        raise ValueError('Either `train_distribute` or'
                         '`experimental_distribute.train_distribute` can be set.')
    config._train_distribute = config._experimental_distribute.train_distribute

if (config._experimental_distribute and
    config._experimental_distribute.eval_distribute):
    if config._eval_distribute:
        raise ValueError('Either `eval_distribute` or'
                         '`experimental_distribute.eval_distribute` can be set.')
    config._eval_distribute = config._experimental_distribute.eval_distribute

cluster_spec = server_lib.ClusterSpec(tf_config.get('cluster', {}))
config._init_distributed_setting_from_environment_var({})

# Use distribute coordinator with STANDALONE_CLIENT mode if
# `experimental_distribute.remote_cluster` is set.
if (config._train_distribute and config._experimental_distribute and
    config._experimental_distribute.remote_cluster):
    if cluster_spec:
        raise ValueError('Cannot set both "cluster_spec" of TF_CONFIG and '
                         '`experimental_distribute.remote_cluster`')
    config._distribute_coordinator_mode = dc.CoordinatorMode.STANDALONE_CLIENT
    config._cluster_spec = config._experimental_distribute.remote_cluster
    logging.info('RunConfig initialized for Distribute Coordinator with '
                 'STANDALONE_CLIENT mode')
    exit()

# Don't use distribute coordinator if it is local training or cluster has a
# MASTER job or `train_distribute` is not specified.
if (not cluster_spec or 'master' in cluster_spec.jobs or
    not config._train_distribute):
    config._distribute_coordinator_mode = None
    config._init_distributed_setting_from_environment_var(tf_config)
    config._maybe_overwrite_session_config_for_distributed_training()
    logging.info('Not using Distribute Coordinator.')
    exit()

# Use distribute coordinator with INDEPENDENT_WORKER mode otherwise.
assert tf_config

# Set the cluster_spec only since the distributed setting will come from
# distribute coordinator.
config._cluster_spec = cluster_spec
config._distribute_coordinator_mode = dc.CoordinatorMode.INDEPENDENT_WORKER
logging.info('RunConfig initialized for Distribute Coordinator with '
             'INDEPENDENT_WORKER mode')
