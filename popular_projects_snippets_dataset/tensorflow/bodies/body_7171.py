# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
traces = []

@def_function.function
def model_fn():
    traces.append(None)

self.assertEmpty(traces)

for i in range(10):
    distribution.extended.call_for_each_replica(model_fn)

    if i == 0:
        num_devices = len(traces)
        self.assertGreater(num_devices, 0)
    else:
        # model_fn should not have been re-evaluated so the length should remain
        # the same.
        self.assertLen(traces, num_devices)
