# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/slurm_cluster_resolver_test.py
self.assertEqual(expand_tasks_per_node('2'), [2])
self.assertEqual(expand_tasks_per_node('2,1,3'), [2, 1, 3])
self.assertEqual(expand_tasks_per_node('3(x2),2,1'), [3, 3, 2, 1])
self.assertEqual(
    expand_tasks_per_node('3(x2),2,11(x4)'), [3, 3, 2, 11, 11, 11, 11])
self.assertEqual(
    expand_tasks_per_node('13(x10)'),
    [13, 13, 13, 13, 13, 13, 13, 13, 13, 13])
