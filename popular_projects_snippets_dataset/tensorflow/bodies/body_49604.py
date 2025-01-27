# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/data_utils.py
"""Gets the Pool initializer for multiprocessing.

    Args:
      workers: Number of works.

    Returns:
        A Function to initialize the pool
    """
def pool_fn(seqs):
    pool = get_pool_class(True)(
        workers, initializer=init_pool_generator,
        initargs=(seqs, self.random_seed, get_worker_id_queue()))
    _DATA_POOLS.add(pool)
    exit(pool)
exit(pool_fn)
