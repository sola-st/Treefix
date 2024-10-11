# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
context = distribute_coordinator_context.get_current_worker_context()
self.assertTrue(context is not None)

self.assertEqual(context._strategy.extended.experimental_should_init,
                 strategy.extended.experimental_should_init)
self.assertEqual(context.should_checkpoint,
                 strategy.extended.should_checkpoint)
self.assertEqual(context.should_save_summary,
                 strategy.extended.should_save_summary)

task_type = str(context.task_type)
task_id = context.task_id or 0
with self._lock:
    if task_type not in self._strategy_property:
        self._strategy_property[task_type] = []
    while len(self._strategy_property[task_type]) <= task_id:
        self._strategy_property[task_type].append(None)
    self._strategy_property[task_type][task_id] = (
        context._strategy.extended.experimental_should_init,
        context.should_checkpoint,
        context.should_save_summary)
