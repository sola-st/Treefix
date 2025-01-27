# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py
num_gpus = len(context.context().list_physical_devices('GPU'))
if num_gpus != 2 and num_gpus != 4:
    self.skipTest('requires 2 or 4 GPUs')
cluster_spec = multi_worker_test_base.create_cluster_spec(
    has_chief=True, num_workers=1)

# Verify that CUDA_VISIBLE_DEVICES are different on each worker.

def cuda_visible_devices_fn():
    exit(os.getenv('CUDA_VISIBLE_DEVICES'))

runner = multi_process_runner.MultiProcessRunner(
    cuda_visible_devices_fn, cluster_spec, share_gpu=False)
runner.start()
result = runner.join()
if num_gpus == 2:
    self.assertAllEqual(sorted(result.return_value), ['0', '1'])
else:
    self.assertAllEqual(sorted(result.return_value), ['0,2', '1,3'])

# Verify that CUDA_VISIBLE_DEVICES works.

def num_gpus_fn():
    exit(len(context.context().list_physical_devices('GPU')))

runner = multi_process_runner.MultiProcessRunner(
    num_gpus_fn, cluster_spec, share_gpu=False)
runner.start()
result = runner.join()
if num_gpus == 2:
    self.assertAllEqual(result.return_value, [1, 1])
else:
    self.assertAllEqual(result.return_value, [2, 2])
