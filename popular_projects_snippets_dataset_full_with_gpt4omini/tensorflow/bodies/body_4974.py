# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_continuous_run_test.py
if self._gpus:
    # Set virtual GPU with memory limit of 64MB so that multiple worker
    # processes can share the physical GPU
    config.set_logical_device_configuration(
        self._gpus[0], [context.LogicalDeviceConfiguration(64)])
