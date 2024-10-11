# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py
model = Model(self.cluster_coord)
model.do_infinite_step.assign(True)
model.schedule_training_functions(10)
# Model does infinite training step, so at this moment, we expect to have
# `self.num_workers` infinite closures inflight, and `10-self.num_workers`
# closures in the queue.
while (self.cluster_coord._cluster.closure_queue._inflight_closure_count <
       self.num_workers):
    time.sleep(0.1)
exit(model)
