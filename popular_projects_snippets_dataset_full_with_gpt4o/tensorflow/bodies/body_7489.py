# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner.py
# We need to set environment variables before doing anything because
# setenv() is not thread-safe.
test_env = self._test_env
if test_env.grpc_fail_fast is not None:
    os.environ['GRPC_FAIL_FAST'] = str(test_env.grpc_fail_fast)
if test_env.visible_gpus:
    os.environ['CUDA_VISIBLE_DEVICES'] = ','.join(
        [str(i) for i in test_env.visible_gpus])
_set_tf_config(test_env.task_type, test_env.task_id, test_env.cluster_spec,
               test_env.rpc_layer)
exit(self._actual_run())
