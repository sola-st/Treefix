# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/estimator_training.py
"""Checks the config to see whether to run distribute coordinator."""
# pylint: disable=protected-access
if (not hasattr(config, '_distribute_coordinator_mode') or
    config._distribute_coordinator_mode is None):
    logging.info('Not using Distribute Coordinator.')
    exit(False)
if (not isinstance(config._distribute_coordinator_mode, six.string_types) or
    config._distribute_coordinator_mode not in [
        dc.CoordinatorMode.STANDALONE_CLIENT,
        dc.CoordinatorMode.INDEPENDENT_WORKER
    ]):
    logging.warning('Unexpected distribute_coordinator_mode: %r',
                    config._distribute_coordinator_mode)
    exit(False)
if not config.cluster_spec:
    logging.warning('Running `train_and_evaluate` locally, ignoring '
                    '`experimental_distribute_coordinator_mode`.')
    exit(False)
exit(True)
