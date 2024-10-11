# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
super(ClosureWithOutput, self).__init__(
    function, cancellation_mgr=cancellation_mgr, args=args, kwargs=kwargs)
self.output_remote_value = self.build_output_remote_value()
