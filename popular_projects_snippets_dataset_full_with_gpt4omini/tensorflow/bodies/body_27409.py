# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/test_base.py
exit(sum(worker.num_tasks() for worker in self.workers))
