# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_cluster_test.py
preemption_key = "TF_DEFAULT_PREEMPTION_NOTICE_KEY"
preemption_task = "/job:worker/task:0"

with ops.device(self.device_t1):
    gen_check_preemption_op.check_preemption(preemption_key=preemption_key)

# Simulate a preemption notifier callback invocation.
context.context().set_config_key_value(preemption_key, preemption_task)
with self.assertRaises(errors.AbortedError) as cm:
    with ops.device(self.device_t2):
        gen_check_preemption_op.check_preemption(preemption_key=preemption_key)
self.assertEqual(
    cm.exception.experimental_payloads.get(
        b"type.googleapis.com/tensorflow.distributed_runtime.WorkerPreemption"
    ), preemption_task.encode())
