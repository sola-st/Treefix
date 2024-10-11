# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
gpus = config.list_logical_devices('GPU')
self.assertNotEqual(len(gpus), 0)

context.ensure_initialized()

gpus = config.list_logical_devices('GPU')
self.assertNotEqual(len(gpus), 0)
for gpu in gpus:
    self.assertIsNotNone(gpu.name)

context.ensure_initialized()

job_name = 'test'
cluster_def = cluster_pb2.ClusterDef()
job_def = cluster_def.job.add()
job_def.name = job_name
job_def.tasks[0] = 'localhost:0'

server_def = tensorflow_server_pb2.ServerDef(
    cluster=cluster_def, job_name=job_name, task_index=0, protocol='grpc')

context.set_server_def(server_def)

gpus = config.list_logical_devices('GPU')
for gpu in gpus:
    self.assertIsNotNone(gpu.name)
