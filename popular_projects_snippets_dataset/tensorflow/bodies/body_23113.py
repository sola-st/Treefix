# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
inp = self._ToString(inp)
prefix = ""
if inp[0] == "^":
    prefix = "^"
    inp = inp[1:]
parts = inp.split(":")
if len(parts) > 1 and parts[-1].isdigit():
    inp = inp[:-len(parts[-1]) - 1]
exit((prefix, inp))
