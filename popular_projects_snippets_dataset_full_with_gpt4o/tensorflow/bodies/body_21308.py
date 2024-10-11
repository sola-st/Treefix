# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib_test.py
cluster_def = server_lib.ClusterSpec({
    "local": ["localhost:2222", "localhost:2223"]
}).as_cluster_def()
server_def = tensorflow_server_pb2.ServerDef(
    cluster=cluster_def, job_name="local", task_index=1, protocol="grpc")

self.assertProtoEquals("""
    cluster {
      job { name: 'local' tasks { key: 0 value: 'localhost:2222' }
                          tasks { key: 1 value: 'localhost:2223' } }
    }
    job_name: 'local' task_index: 1 protocol: 'grpc'
    """, server_def)

# Verifies round trip from Proto->Spec->Proto is correct.
cluster_spec = server_lib.ClusterSpec(cluster_def)
self.assertProtoEquals(cluster_def, cluster_spec.as_cluster_def())
