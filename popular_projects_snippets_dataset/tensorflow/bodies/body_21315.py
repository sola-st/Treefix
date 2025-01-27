# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib_test.py
original_dict = {
    "ps": ["ps0:2222", "ps1:2222"],
    "worker": ["worker0:2222", "worker1:2222", "worker2:2222"],
    "sparse": {
        0: "sparse0:2222",
        3: "sparse3:2222"
    }
}
cluster_spec = server_lib.ClusterSpec(original_dict)

self.assertEqual(original_dict, cluster_spec.as_dict())

self.assertEqual(2, cluster_spec.num_tasks("ps"))
self.assertEqual(3, cluster_spec.num_tasks("worker"))
self.assertEqual(2, cluster_spec.num_tasks("sparse"))
with self.assertRaises(ValueError):
    cluster_spec.num_tasks("unknown")

self.assertEqual("ps0:2222", cluster_spec.task_address("ps", 0))
self.assertEqual("sparse0:2222", cluster_spec.task_address("sparse", 0))
with self.assertRaises(ValueError):
    cluster_spec.task_address("unknown", 0)
with self.assertRaises(ValueError):
    cluster_spec.task_address("sparse", 2)

self.assertEqual([0, 1], cluster_spec.task_indices("ps"))
self.assertEqual([0, 1, 2], cluster_spec.task_indices("worker"))
self.assertEqual([0, 3], cluster_spec.task_indices("sparse"))
with self.assertRaises(ValueError):
    cluster_spec.task_indices("unknown")

# NOTE(mrry): `ClusterSpec.job_tasks()` is not recommended for use
# with sparse jobs.
self.assertEqual(["ps0:2222", "ps1:2222"], cluster_spec.job_tasks("ps"))
self.assertEqual(["worker0:2222", "worker1:2222", "worker2:2222"],
                 cluster_spec.job_tasks("worker"))
self.assertEqual(["sparse0:2222", None, None, "sparse3:2222"],
                 cluster_spec.job_tasks("sparse"))
with self.assertRaises(ValueError):
    cluster_spec.job_tasks("unknown")
