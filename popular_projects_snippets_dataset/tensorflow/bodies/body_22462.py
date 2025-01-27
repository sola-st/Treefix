# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
if self._final_ops is not None:
    try:
        self._final_ops_values = session.run(
            self._final_ops, feed_dict=self._final_ops_feed_dict)
    except (errors.OutOfRangeError, StopIteration) as e:
        logging.warning(
            "An OutOfRangeError or StopIteration exception is raised by the "
            "code in FinalOpsHook. This typically means the Ops running by the "
            "FinalOpsHook have a dependency back to some input source, which "
            "should not happen. For example, for metrics in "
            "tf.estimator.Estimator, all metrics functions return two Ops: "
            "`value_op` and  `update_op`. Estimator.evaluate calls the "
            "`update_op` for each batch of the data in input source and, once "
            "it is exhausted, it call the `value_op` to get the metric values. "
            "The `value_op` here should have dependency back to variables "
            "reading only, rather than reading another batch from input. "
            "Otherwise, the `value_op`, executed by `FinalOpsHook`, triggers "
            "another data reading, which ends OutOfRangeError/StopIteration. "
            "Please fix that.")
        raise e
