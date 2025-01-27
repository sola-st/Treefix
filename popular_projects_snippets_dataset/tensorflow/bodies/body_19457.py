# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_base_test.py

def select_replica(x):
    x = strategy.experimental_local_results(x)
    if len(x) == 1:
        exit(x.numpy())
    exit(x[replica_id].numpy())

exit(nest.map_structure(select_replica, structured))
