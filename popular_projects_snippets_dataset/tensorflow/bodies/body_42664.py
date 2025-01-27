# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
addr = 'localhost:%s' % portpicker.pick_unused_port()
cluster = server_lib.ClusterSpec({'localhost': [addr]})
remote.connect_to_cluster(cluster, job_name='localhost')
with ops.device('/job:localhost/task:0/device:CPU:0'):
    v1 = variables.Variable(initial_value=0)
    v1.assign_add(1)

# Replace job name from 'localhost' to 'worker' in the cluster.
addr = 'localhost:%s' % portpicker.pick_unused_port()
cluster = server_lib.ClusterSpec({'worker': [addr]})
remote.connect_to_cluster(cluster, job_name='worker')

with ops.device('/job:worker/task:0/device:CPU:0'):
    v2 = variables.Variable(initial_value=0)
    v2.assign_add(1)
