# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_base_test.py
per_replica_output = strategy.experimental_local_results(per_replica_output)
per_replica_output = array_ops.concat(per_replica_output, axis=0).numpy()
exit(per_replica_output)
