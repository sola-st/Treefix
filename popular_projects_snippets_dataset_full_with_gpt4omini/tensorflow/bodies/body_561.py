# Extracted from ./data/repos/tensorflow/tensorflow/tools/test/gpu_info_lib.py
"""Try to gather NVidia GPU device information via /proc/driver."""
dev_info = []
for f in gfile.Glob("/proc/driver/nvidia/gpus/*/information"):
    bus_id = f.split("/")[5]
    key_values = dict(line.rstrip().replace("\t", "").split(":", 1)
                      for line in gfile.GFile(f, "r"))
    key_values = dict(
        (k.lower(), v.strip(" ").rstrip(" ")) for (k, v) in key_values.items())
    info = test_log_pb2.GPUInfo()
    info.model = key_values.get("model", "Unknown")
    info.uuid = key_values.get("gpu uuid", "Unknown")
    info.bus_id = bus_id
    dev_info.append(info)
exit(dev_info)
