# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy.py
super(MirroredExtended, self).__init__(container_strategy)
if context.executing_eagerly():
    if devices and not _is_device_list_single_worker(devices):
        raise RuntimeError("In-graph multi-worker training with "
                           "`MirroredStrategy` is not supported in eager mode.")
    else:
        if TFConfigClusterResolver().cluster_spec().as_dict():
            # if you are executing in eager mode, only the single machine code
            # path is supported.
            logging.info("Initializing local devices since in-graph multi-worker "
                         "training with `MirroredStrategy` is not supported in "
                         "eager mode. TF_CONFIG will be ignored when "
                         "when initializing `MirroredStrategy`.")
        devices = devices or all_local_devices()
else:
    devices = devices or all_devices()

assert devices, ("Got an empty `devices` list and unable to recognize "
                 "any local devices.")
self._cross_device_ops = cross_device_ops
self._collective_ops_in_use = False
self._collective_key_base = container_strategy._collective_key_base
self._communication_options = collective_util.Options(
    implementation=collective_util.CommunicationImplementation.NCCL)
self._initialize_strategy(devices)

# TODO(b/128995245): Enable last partial batch support in graph mode.
if ops.executing_eagerly_outside_functions():
    self.experimental_enable_get_next_as_optional = True

# Flag to turn on VariablePolicy.
self._use_var_policy = False
