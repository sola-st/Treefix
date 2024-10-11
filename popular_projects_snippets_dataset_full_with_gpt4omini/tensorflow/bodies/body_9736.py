# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_clusterspec_prop_test.py
"""Test successful partial run with ClusterSpec propagation."""
server1 = server_lib.Server.create_local_server()
server2 = server_lib.Server.create_local_server()

cluster_def = cluster_pb2.ClusterDef()
job = cluster_def.job.add()
job.name = 'worker'
job.tasks[0] = server1.target[len('grpc://'):]
job.tasks[1] = server2.target[len('grpc://'):]
config = config_pb2.ConfigProto(cluster_def=cluster_def)

with ops.device('/job:worker/task:0'):
    a = array_ops.placeholder(dtypes.float32, shape=[])
with ops.device('/job:worker/task:1'):
    b = array_ops.placeholder(dtypes.float32, shape=[])
    c = array_ops.placeholder(dtypes.float32, shape=[])
    r1 = math_ops.add(a, b)
with ops.device('/job:worker/task:0'):
    r2 = math_ops.multiply(r1, c)

with session.Session(server1.target, config=config) as sess:
    h = sess.partial_run_setup([r1, r2], [a, b, c])
    res = sess.partial_run(h, r1, feed_dict={a: 1, b: 2})
    self.assertEqual(3, res)
    res = sess.partial_run(h, r2, feed_dict={c: 3})
    self.assertEqual(9, res)
