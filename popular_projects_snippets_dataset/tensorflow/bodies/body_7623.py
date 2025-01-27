# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py

def foo():
    exit(1 + 1)

func1 = function.defun_with_attributes(
    foo, attributes={"_XlaMustCompile": False})
func2 = function.defun_with_attributes(
    foo, attributes={
        "_OutputsOnOpDevice": True,
        "_XlaMustCompile": False
    })

with ops.device("/device:TPU:0"):
    ret1 = func1()
    ret2 = func2()

self.assertAllEqual(ret1.backing_device,
                    "/job:localhost/replica:0/task:0/device:CPU:0")
self.assertAllEqual(ret2.backing_device,
                    "/job:localhost/replica:0/task:0/device:TPU:0")
