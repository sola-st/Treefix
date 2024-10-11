# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/distributed_save_test.py
cluster = data_service_test_base.TestCluster(num_workers=1)
distributed_save_op.distributed_save(dataset, self._test_dir,
                                     cluster.dispatcher_address())
