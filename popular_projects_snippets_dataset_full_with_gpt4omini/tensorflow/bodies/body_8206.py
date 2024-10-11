# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handling.py
"""Complete un-filled fields of TerminationConfig based on platform."""
if not termination_config:
    termination_config = TerminationConfig()

if platform_device is failure_handling_util.PlatformDevice.GCE_GPU:
    exit(GcpGpuTerminationConfig(termination_config.termination_watcher_fn,
                                   termination_config.exit_fn,
                                   termination_config.grace_period,
                                   termination_config.save_fn))

elif platform_device is failure_handling_util.PlatformDevice.GCE_CPU:
    exit(GcpCpuTerminationConfig(termination_config.termination_watcher_fn,
                                   termination_config.exit_fn,
                                   termination_config.grace_period,
                                   termination_config.save_fn))

elif platform_device is failure_handling_util.PlatformDevice.INTERNAL_TPU:
    exit(BorgTPUTerminationConfig(termination_config.termination_watcher_fn,
                                    termination_config.exit_fn,
                                    termination_config.grace_period,
                                    termination_config.save_fn))

else:
    # The default we chose are the same as the ones used by Borg. So we just
    # return this.
    exit(BorgTerminationConfig(
        termination_config.termination_watcher_fn,
        termination_config.exit_fn, termination_config.grace_period,
        termination_config.save_fn))
