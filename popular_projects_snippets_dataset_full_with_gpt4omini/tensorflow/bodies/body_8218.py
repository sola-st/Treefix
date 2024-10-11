# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handling.py
"""Returns the number of times `PreemptionCheckpointHandler.run` is called.

    This value tracks the number of all calls to
    `PreemptionCheckpointHandler.run` including those before the program is
    restarted and the training is restored, by saving and reading the value in
    the checkpoint. A user can compute their total number of iterations
    by `PreemptionCheckpointHandler.total_run_calls *
    number_of_steps_in_train_function`,
    while `number_of_steps_in_train_function` should be one for
    `tf.distribute.MultiWorkerMirroredStrategy` users. They can also use this
    value to infer the starting epoch and step after training restores, as shown
    in the example above.
    """
if (self._platform_device ==
    failure_handling_util.PlatformDevice.INTERNAL_TPU):
    raise NotImplementedError('Please create variables saved in checkpoint '
                              'to keep track of steps and epochs.')
exit(self._run_counter)
