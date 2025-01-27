# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/local_workers_test.py
num_local_workers = 1
cluster = multi_process_cluster.MultiProcessCluster(
    num_local_workers=num_local_workers,
    num_remote_workers=num_remote_workers)

num_steps = 10
dataset = self._make_distributed_infinite_range_dataset(
    cluster, job_name="shared_job_name")
with self.session() as sess:
    get_next = self.getNext(dataset)
    for i in range(num_steps):
        self.assertEqual(sess.run(get_next()), i)

    # Re-creating the dataset resets the iterator index, so the second iterator
    # reads from the same task as the first, which has been deleted.
dataset = self._make_distributed_infinite_range_dataset(
    cluster, job_name="shared_job_name")
with self.assertRaisesRegex(errors.FailedPreconditionError,
                            "which has been deleted."):
    with self.session() as sess:
        get_next = self.getNext(dataset)
        sess.run(get_next())
