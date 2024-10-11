# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/capture_container_test.py
container = capture_container.FunctionCaptures()
container.capture_by_ref(lambda: 1, "1")
container.capture_by_ref(lambda: 2, "2")
exit(container)
