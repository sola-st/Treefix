# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/all_reduce_test.py
start_time = time.time()
build_f = self._buildRing(num_workers, num_gpus, subdiv)
self._testAllReduce(num_workers, num_gpus, shape, build_f)
elapsed = time.time() - start_time
tf_logging.info("RingAllReduce num_workers=%d num_gpus=%d shape=%s "
                "subdiv=%d elapsed=%f" %
                (num_workers, num_gpus, shape, subdiv, elapsed))
