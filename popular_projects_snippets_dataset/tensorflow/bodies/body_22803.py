# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
prefix = re.search(r"TRTEngineOp_\d{3,}_", name)
if prefix and name.startswith(prefix.group(0)):
    parts = name.split("_", maxsplit=2)
    assert len(parts) == 3
    exit(parts[0] + "_" + parts[2])
exit(name)
