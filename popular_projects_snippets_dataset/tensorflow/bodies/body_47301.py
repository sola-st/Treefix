# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_file_utils.py
task_id = strategy.extended._task_id  # pylint: disable=protected-access
exit('workertemp_' + str(task_id))
