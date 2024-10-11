# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
context.context().configure_coordination_service(
    service_type='standalone', service_leader='/job:my_ps/replica:0/task:0')
remote.connect_to_cluster(self._cluster)
context.context().ensure_initialized()

states = context.context().get_task_states([('my_worker', 2), ('my_ps', 2)])
self.assertLen(states, 4)
for state in states:
    self.assertIsNone(state)
