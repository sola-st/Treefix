# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/datasets_test.py
super(DatasetsTest, self).setUp()
self._coord = server_lib.Server.create_local_server()
self._worker = server_lib.Server.create_local_server()

self._cluster_def = cluster_pb2.ClusterDef()
worker_job = self._cluster_def.job.add()
worker_job.name = 'worker'
worker_job.tasks[0] = self._worker.target[len('grpc://'):]
coord_job = self._cluster_def.job.add()
coord_job.name = 'coordinator'
coord_job.tasks[0] = self._coord.target[len('grpc://'):]

session_config = config_pb2.ConfigProto(cluster_def=self._cluster_def)

self._sess = session.Session(self._worker.target, config=session_config)
self._worker_device = '/job:' + worker_job.name
