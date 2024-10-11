# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/cluster_test.py
with cluster.Provision() as gcluster:
    op_names = gcluster.ListAvailableOps()
    self.assertTrue('Add' in op_names)
    self.assertTrue('MatMul' in op_names)
    self.assertEqual(op_names, sorted(op_names))
