# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib_test.py
cluster_def = server_lib.ClusterSpec({
    "ps": ["ps0:2222", "ps1:2222"],
    "worker": ["worker0:2222", "worker1:2222", "worker2:2222"]
}).as_cluster_def()
server_def = tensorflow_server_pb2.ServerDef(
    cluster=cluster_def, job_name="worker", task_index=2, protocol="grpc")

self.assertProtoEquals("""
    cluster {
      job { name: 'ps' tasks { key: 0 value: 'ps0:2222' }
                       tasks { key: 1 value: 'ps1:2222' } }
      job { name: 'worker' tasks { key: 0 value: 'worker0:2222' }
                           tasks { key: 1 value: 'worker1:2222' }
                           tasks { key: 2 value: 'worker2:2222' } }
    }
    job_name: 'worker' task_index: 2 protocol: 'grpc'
    """, server_def)

# Verifies round trip from Proto->Spec->Proto is correct.
cluster_spec = server_lib.ClusterSpec(cluster_def)
self.assertProtoEquals(cluster_def, cluster_spec.as_cluster_def())
