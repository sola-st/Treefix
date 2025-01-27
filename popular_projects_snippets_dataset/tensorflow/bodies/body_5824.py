# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/slurm_cluster_resolver_test.py
self.assertEqual(expand_hostlist('n1'), ['n1'])
self.assertEqual(expand_hostlist('n[1,3]'), ['n1', 'n3'])
self.assertEqual(expand_hostlist('n[1-3]'), ['n1', 'n2', 'n3'])
self.assertEqual(
    expand_hostlist('n[1-2],m5,o[3-4,6,7-9]'),
    ['n1', 'n2', 'm5', 'o3', 'o4', 'o6', 'o7', 'o8', 'o9'])
self.assertEqual(
    expand_hostlist('n[0001-0003],m5,o[009-011]'),
    ['n0001', 'n0002', 'n0003', 'm5', 'o009', 'o010', 'o011'])
