# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with self.cached_session():
    handle = test_ops.stub_resource_handle_op(container="a", shared_name="b")
    resources.register_resource(
        handle=handle,
        create_op=test_ops.resource_create_op(handle),
        is_initialized_op=test_ops.resource_initialized_op(handle))
    self.assertEqual(
        len(
            resources.report_uninitialized_resources(
                resources.shared_resources()).eval()), 1)
    resources.initialize_resources(resources.shared_resources()).run()
    self.assertEqual(
        len(
            resources.report_uninitialized_resources(
                resources.shared_resources()).eval()), 0)
