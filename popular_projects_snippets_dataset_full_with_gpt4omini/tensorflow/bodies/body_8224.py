# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handling.py
"""Saves the checkpoint and exit program."""
distribution_strategy_api_counter.get_cell(
    self._platform_device.name,
    'PreemptionCheckpointHandler Saving Checkpoint').increase_by(1)
logging.info('PreemptionCheckpointHandler: Starting saving a checkpoint.')

if self._platform_device != failure_handling_util.PlatformDevice.INTERNAL_TPU:
    self._checkpointed_runs.assign(self.total_run_calls)

start_time = time.monotonic()

if self._save_fn:
    self._save_fn(*args, **kwargs)
else:
    self._write_checkpoint_manager.save(*args, **kwargs)

end_time = time.monotonic()

logging.info('Checkpoint finished at path %s',
             self._write_checkpoint_manager.directory)
self._checkpoint_time = end_time - start_time
