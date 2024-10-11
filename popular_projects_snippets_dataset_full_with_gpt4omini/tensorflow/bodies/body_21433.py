# Extracted from ./data/repos/tensorflow/tensorflow/python/training/sync_replicas_optimizer_test.py
num_workers = 2
replicas_to_aggregate = 2
num_ps = 2
workers, _ = create_local_cluster(num_workers=num_workers, num_ps=num_ps)

# Creates and returns all the workers.
sessions, graphs, train_ops = get_workers(num_workers,
                                          replicas_to_aggregate, workers)

# Chief should have already initialized all the variables.
var_0_g_0 = graphs[0].get_tensor_by_name("v0:0")
var_1_g_0 = graphs[0].get_tensor_by_name("v1:0")
local_step_0 = graphs[0].get_tensor_by_name("sync_rep_local_step:0")
self.assertAllEqual(0.0, sessions[0].run(var_0_g_0))
self.assertAllEqual(1.0, sessions[0].run(var_1_g_0))
self.assertAllEqual(0, sessions[0].run(local_step_0))

# Will just use session 1 to verify all the variables later.
var_0_g_1 = graphs[1].get_tensor_by_name("v0:0")
var_1_g_1 = graphs[1].get_tensor_by_name("v1:0")
var_sparse_g_1 = graphs[1].get_tensor_by_name("v_sparse:0")
local_step_1 = graphs[1].get_tensor_by_name("sync_rep_local_step:0")
global_step = graphs[1].get_tensor_by_name("global_step:0")

# The steps should also be initialized.
self.assertAllEqual(0, sessions[1].run(global_step))
self.assertAllEqual(0, sessions[1].run(local_step_1))
self.assertAllClose([[3.0], [4.0]], sessions[1].run(var_sparse_g_1))

# We have initial tokens in the queue so we can call this one by one. After
# the first step, this will no longer work as there will be no more extra
# tokens in the queue.
sessions[0].run(train_ops[0])
sessions[1].run(train_ops[1])

# The global step should have been updated and the variables should now have
# the new values after the average of the gradients are applied.
while sessions[1].run(global_step) != 1:
    time.sleep(0.01)

self.assertAllClose(0 - (0.1 + 0.3) / 2 * 2.0, sessions[1].run(var_0_g_1))
self.assertAllClose(1 - (0.9 + 1.1) / 2 * 2.0, sessions[1].run(var_1_g_1))
self.assertAllClose([[3.0], [4.0 - (0.1 + 0.3) / 2 * 2.0]],
                    sessions[1].run(var_sparse_g_1))

# The local step for both workers should still be 0 because the initial
# tokens in the token queue are 0s. This means that the following
# computation of the gradients will be wasted as local_step is smaller than
# the current global step. However, this only happens once when the system
# just starts and this is necessary to make the system robust for the case
# when chief gets restarted by errors/preemption/...
self.assertAllEqual(0, sessions[0].run(local_step_0))
self.assertAllEqual(0, sessions[1].run(local_step_1))

sessions[0].run(train_ops[0])
sessions[1].run(train_ops[1])
# Although the global step should still be 1 as explained above, the local
# step should now be updated to 1. The variables are still the same.
self.assertAllEqual(1, sessions[1].run(global_step))
self.assertAllEqual(1, sessions[0].run(local_step_0))
self.assertAllEqual(1, sessions[1].run(local_step_1))
self.assertAllClose(0 - (0.1 + 0.3) / 2 * 2.0, sessions[1].run(var_0_g_1))
self.assertAllClose(1 - (0.9 + 1.1) / 2 * 2.0, sessions[1].run(var_1_g_1))

# At this step, the token queue is empty. So the 2 workers need to work
# together to proceed.
threads = []
threads.append(
    self.checkedThread(
        target=self._run, args=(train_ops[0], sessions[0])))
threads.append(
    self.checkedThread(
        target=self._run, args=(train_ops[1], sessions[1])))

# The two workers starts to execute the train op.
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

# The global step should now be 2 and the gradients should have been
# applied twice.
self.assertAllEqual(2, sessions[1].run(global_step))
self.assertAllClose(0 - 2 * (0.1 + 0.3) / 2 * 2.0,
                    sessions[1].run(var_0_g_1))
self.assertAllClose(1 - 2 * (0.9 + 1.1) / 2 * 2.0,
                    sessions[1].run(var_1_g_1))
