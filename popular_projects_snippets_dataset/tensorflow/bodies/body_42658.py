# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
super(MultiJobsTest, self).setUp()

workers, ps = test_util.create_local_cluster(num_workers=2, num_ps=2)
cluster = {
    'my_worker': [_strip_prefix(t.target, _GRPC_PREFIX) for t in workers],
    'my_ps': [_strip_prefix(t.target, _GRPC_PREFIX) for t in ps],
}
self._cluster = server_lib.ClusterSpec(cluster)
self._cluster_resolver = SimpleClusterResolver(
    cluster_spec=self._cluster, master=ps[0].target)
