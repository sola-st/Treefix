# Extracted from ./data/repos/tensorflow/tensorflow/python/training/sync_replicas_optimizer_test.py
num_workers = 3
replicas_to_aggregate = 2
num_ps = 2
workers, _ = create_local_cluster(num_workers=num_workers, num_ps=num_ps)

# Creates and returns all the workers.
sessions, graphs, train_ops = get_workers(num_workers,
                                          replicas_to_aggregate, workers)

# Chief should have already initialized all the variables.
var_0_g_1 = graphs[1].get_tensor_by_name("v0:0")
var_1_g_1 = graphs[1].get_tensor_by_name("v1:0")
local_step_1 = graphs[1].get_tensor_by_name("sync_rep_local_step:0")
global_step = graphs[1].get_tensor_by_name("global_step:0")

# The steps should also be initialized.
self.assertAllEqual(0, sessions[1].run(global_step))
self.assertAllEqual(0, sessions[1].run(local_step_1))

# We have initial tokens in the queue so we can call this one by one. After
# the token queue becomes empty, they should be called concurrently.
# Here worker 0 and worker 2 finished first.
sessions[0].run(train_ops[0])
sessions[2].run(train_ops[2])

# The global step should have been updated since we only need to collect 2
# gradients. The variables should now have the new values after the average
# of the gradients from worker 0/2 are applied.
while sessions[1].run(global_step) != 1:
    time.sleep(0.01)

self.assertAllEqual(1, sessions[1].run(global_step))
self.assertAllClose(0 - (0.1 + 0.5) / 2 * 2.0, sessions[1].run(var_0_g_1))
self.assertAllClose(1 - (0.9 + 1.3) / 2 * 2.0, sessions[1].run(var_1_g_1))

# Worker 1 finished later and its gradients will now be dropped as it is
# stale.
sessions[1].run(train_ops[1])

# As shown in the previous test, the local_step for all workers should be
# still 0 so their next computation will also be dropped.
sessions[0].run(train_ops[0])
sessions[1].run(train_ops[1])
sessions[2].run(train_ops[2])

# Although the global step should still be 1 as explained above, the local
# step should now be updated to 1. Just check worker 1 as an example.
self.assertAllEqual(1, sessions[1].run(global_step))
self.assertAllEqual(1, sessions[1].run(local_step_1))

thread_0 = self.checkedThread(
    target=self._run, args=(train_ops[0], sessions[0]))
thread_1 = self.checkedThread(
    target=self._run, args=(train_ops[1], sessions[1]))

# Lets worker 0 execute first.
# It will wait as we need 2 workers to finish this step and the global step
# should be still 1.
thread_0.start()
self.assertAllEqual(1, sessions[1].run(global_step))

# Starts worker 1.
thread_1.start()
thread_1.join()
thread_0.join()

# The global step should now be 2 and the gradients should have been
# applied again.
self.assertAllEqual(2, sessions[1].run(global_step))
self.assertAllClose(-0.6 - (0.1 + 0.3) / 2 * 2.0,
                    sessions[1].run(var_0_g_1))
self.assertAllClose(-1.2 - (0.9 + 1.1) / 2 * 2.0,
                    sessions[1].run(var_1_g_1))
