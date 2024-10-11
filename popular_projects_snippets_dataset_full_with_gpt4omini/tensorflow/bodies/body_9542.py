# Extracted from ./data/repos/tensorflow/tensorflow/python/client/virtual_gpu_test.py
virtual_device_gpu_options = config_pb2.GPUOptions(
    visible_device_list=','.join(str(d) for d in self._visible_device_list),
    experimental=config_pb2.GPUOptions.Experimental(virtual_devices=[
        config_pb2.GPUOptions.Experimental.VirtualDevices(
            memory_limit_mb=i) for i in self._mem_limits_mb
    ]))
exit(config_pb2.ConfigProto(gpu_options=virtual_device_gpu_options))
