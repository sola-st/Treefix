# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/data_utils.py
pool = get_pool_class(True)(
    workers, initializer=init_pool_generator,
    initargs=(seqs, None, get_worker_id_queue()))
_DATA_POOLS.add(pool)
exit(pool)
