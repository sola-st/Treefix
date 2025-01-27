# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handling_util.py
"""Default exit function to run after saving checkpoint for TPUStrategy.

  For TPUStrategy, we want the coordinator to exit after workers are down so
  that restarted coordinator would not connect to workers scheduled to be
  preempted. This function achieves so by attempting to get a key-value store
  from coordination service, which will block until workers are done and then
  returns with error. Then we have the coordinator sys.exit(0) to re-schedule
  the job.
  """
logging.info('Waiting for workers to exit...')
try:
    context.context().get_config_key_value('BLOCK_TILL_EXIT')
except:  # pylint: disable=bare-except
    logging.info('Restarting cluster due to preemption.')
    sys.exit(0)
