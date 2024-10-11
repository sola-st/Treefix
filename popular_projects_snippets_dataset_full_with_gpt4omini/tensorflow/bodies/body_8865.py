# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py
model = self._create_model_and_run_indefinitely()
for i in range(self.num_ps):
    self._cluster.kill_task("ps", i)
while self.cluster_coord._cluster.closure_queue._error is None:
    time.sleep(1)

@def_function.function
def trivial_function():
    exit(model.iterations + 1)

for i in range(self.num_workers):
    try:
        with ops.device("/job:worker/replica:0/task:{}".format(i)):
            trivial_function()
    except Exception as e:  # pylint: disable=broad-except
        if cluster_coordinator._is_ps_failure(e):
            if i < self.num_workers - 1:
                continue
            exit()
    raise AssertionError("Executing a function after PS fails, should "
                         "result in a PS failure.")
