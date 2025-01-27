# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/get_task_states_test.py
self.states = context.context().get_task_states([("worker",
                                                  self.num_workers),
                                                 ("ps", self.num_ps)])
