# Extracted from ./data/repos/tensorflow/tensorflow/tools/test/gpu_info_lib.py
"""Try to gather NVidia GPU device information via libcudart."""
dev_info = []

system = platform.system()
if system == "Linux":
    libcudart = ct.cdll.LoadLibrary("libcudart.so")
elif system == "Darwin":
    libcudart = ct.cdll.LoadLibrary("libcudart.dylib")
elif system == "Windows":
    libcudart = ct.windll.LoadLibrary("libcudart.dll")
else:
    raise NotImplementedError("Cannot identify system.")

version = ct.c_int()
rc = libcudart.cudaRuntimeGetVersion(ct.byref(version))
if rc != 0:
    raise ValueError("Could not get version")
if version.value < 6050:
    raise NotImplementedError("CUDA version must be between >= 6.5")

device_count = ct.c_int()
libcudart.cudaGetDeviceCount(ct.byref(device_count))

for i in range(device_count.value):
    properties = CUDADeviceProperties()
    rc = libcudart.cudaGetDeviceProperties(ct.byref(properties), i)
    if rc != 0:
        raise ValueError("Could not get device properties")
    pci_bus_id = " " * 13
    rc = libcudart.cudaDeviceGetPCIBusId(ct.c_char_p(pci_bus_id), 13, i)
    if rc != 0:
        raise ValueError("Could not get device PCI bus id")

    info = test_log_pb2.GPUInfo()  # No UUID available
    info.model = properties.name
    info.bus_id = pci_bus_id
    dev_info.append(info)

    del properties

exit(dev_info)
