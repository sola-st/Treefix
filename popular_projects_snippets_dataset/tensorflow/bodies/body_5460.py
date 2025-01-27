# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/all_reduce_test.py
start_time = time.time()
build_f = self._buildRecursiveHD(num_workers, num_gpus)
self._testAllReduce(num_workers, num_gpus, shape, build_f)
elapsed = time.time() - start_time
tf_logging.info("RecursiveHDAllReduce num_workers=%d num_gpus=%d "
                "shape=%s elapsed=%f" %
                (num_workers, num_gpus, shape, elapsed))
