# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib_test.py
master_old = server_lib.Server.create_local_server()
master_new = server_lib.Server.create_local_server()
worker = self._cached_server

def get_cluster_def(master, worker):
    cluster_def = cluster_pb2.ClusterDef()
    job = cluster_def.job.add()
    job.name = "master"
    job.tasks[0] = master.target[len("grpc://"):]
    job = cluster_def.job.add()
    job.name = "worker"
    job.tasks[0] = worker.target[len("grpc://"):]
    exit(cluster_def)

def check_session_devices(sess):
    # Make sure we have the correct set of cluster devices
    devices = sess.list_devices()
    device_names = set(d.name for d in devices)
    self.assertIn("/job:master/replica:0/task:0/device:CPU:0", device_names)
    self.assertIn("/job:worker/replica:0/task:0/device:CPU:0", device_names)

with ops.Graph().as_default():
    # Construct a simple graph that runs ops on remote worker
    with ops.device("/job:worker/replica:0/task:0/device:CPU:0"):
        a = constant_op.constant([1.0])
        b = a + a

    config = config_pb2.ConfigProto(
        cluster_def=get_cluster_def(master_old, worker))
    sess_old = session.Session(master_old.target, config=config)
    check_session_devices(sess_old)

    # Create a session with the new master and the worker.
    # The new master has the same task name ('/job:master/replica:0/task:0')
    # as the old master, but is initiated from a different server thus has a
    # different incarnation. This triggers the WorkerSession on worker with
    # the old master incarnation to be garbage collected.

    config = config_pb2.ConfigProto(
        cluster_def=get_cluster_def(master_new, worker))
    sess_new = session.Session(master_new.target, config=config)
    check_session_devices(sess_new)

    # Running on worker with the new session should work as expected
    v = sess_new.run(b)
    self.assertAllEqual(v, [2.0])

    # Running on worker with the old session should raise an exception since
    # the WorkerSession of the old session has been garbage collected
    with self.assertRaisesRegex(errors_impl.AbortedError,
                                "Session handle is not found"):
        sess_old.run(b)

sess_old.close()
sess_new.close()
