# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_cluster_test.py
super(DynamicClusterTest, self).__init__(methodName)
self._cached_server1 = server_lib.Server.create_local_server()
self._cached_server2 = server_lib.Server.create_local_server()
self._cached_server3 = server_lib.Server.create_local_server()
self._cached_server4 = server_lib.Server.create_local_server()

self._cached_server1_target = self._cached_server1.target[len("grpc://"):]
self._cached_server2_target = self._cached_server2.target[len("grpc://"):]
self._cached_server3_target = self._cached_server3.target[len("grpc://"):]
self._cached_server4_target = self._cached_server4.target[len("grpc://"):]

self.server_def_s1 = get_server_def(
    JOB_NAME,
    local_server_port=0,
    remote_server_addresses=[self._cached_server1_target],
    task_index=0)
self.server_def_s1_s2 = get_server_def(
    JOB_NAME,
    local_server_port=0,
    remote_server_addresses=[
        self._cached_server1_target, self._cached_server2_target
    ],
    task_index=0)
self.server_def_s1_s3 = get_server_def(
    JOB_NAME,
    local_server_port=0,
    remote_server_addresses=[
        self._cached_server1_target, self._cached_server3_target
    ],
    task_index=0)
self.server_def_s4_s3 = get_server_def(
    JOB_NAME,
    local_server_port=0,
    remote_server_addresses=[
        self._cached_server4_target, self._cached_server3_target
    ],
    task_index=0)
self.server_def_s1_s2_s3 = get_server_def(
    JOB_NAME,
    local_server_port=0,
    remote_server_addresses=[
        self._cached_server1_target, self._cached_server2_target,
        self._cached_server3_target
    ],
    task_index=0)
self.server_def_s1_s2_s3_s4 = get_server_def(
    JOB_NAME,
    local_server_port=0,
    remote_server_addresses=[
        self._cached_server1_target, self._cached_server2_target,
        self._cached_server3_target, self._cached_server4_target
    ],
    task_index=0)

self.device_local = "/job:%s/replica:0/task:0/device:CPU:0" % JOB_NAME
self.device_t1 = "/job:%s/replica:0/task:1/device:CPU:0" % JOB_NAME
self.device_t2 = "/job:%s/replica:0/task:2/device:CPU:0" % JOB_NAME
self.device_t3 = "/job:%s/replica:0/task:3/device:CPU:0" % JOB_NAME
self.device_t4 = "/job:%s/replica:0/task:4/device:CPU:0" % JOB_NAME
