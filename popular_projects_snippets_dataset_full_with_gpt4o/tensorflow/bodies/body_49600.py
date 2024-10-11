# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/data_utils.py
"""Initializer function for pool workers.

  Args:
    gens: State which should be made available to worker processes.
    random_seed: An optional value with which to seed child processes.
    id_queue: A multiprocessing Queue of worker ids. This is used to indicate
      that a worker process was created by Keras and can be terminated using
      the cleanup_all_keras_forkpools utility.
  """
global _SHARED_SEQUENCES
_SHARED_SEQUENCES = gens

worker_proc = multiprocessing.current_process()

# name isn't used for anything, but setting a more descriptive name is helpful
# when diagnosing orphaned processes.
worker_proc.name = 'Keras_worker_{}'.format(worker_proc.name)

if random_seed is not None:
    np.random.seed(random_seed + worker_proc.ident)

if id_queue is not None:
    # If a worker dies during init, the pool will just create a replacement.
    id_queue.put(worker_proc.ident, block=True, timeout=0.1)
