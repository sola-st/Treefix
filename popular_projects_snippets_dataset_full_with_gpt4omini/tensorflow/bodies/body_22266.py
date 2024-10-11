# Extracted from ./data/repos/tensorflow/tensorflow/python/training/localhost_cluster_performance_test.py
workers, _ = test.create_local_cluster(num_workers=2, num_ps=2)
worker_sessions = [session_lib.Session(w.target) for w in workers]
with ops.device("/job:ps/task:0"):
    var0 = variables.Variable(0.0)
with ops.device("/job:ps/task:1"):
    var1 = variables.Variable(1.0)
worker_sessions[0].run([var0.initializer, var1.initializer])
with ops.device("/job:ps/task:0"):
    var2 = variables.Variable(2.0)
with ops.device("/job:ps/task:1"):
    var3 = variables.Variable(3.0)
worker_sessions[1].run([var2.initializer, var3.initializer])

# Read values back in the opposite session
self.assertAllEqual(0.0, var0.eval(session=worker_sessions[1]))
self.assertAllEqual(1.0, var1.eval(session=worker_sessions[1]))
self.assertAllEqual(2.0, var2.eval(session=worker_sessions[0]))
self.assertAllEqual(3.0, var3.eval(session=worker_sessions[0]))
