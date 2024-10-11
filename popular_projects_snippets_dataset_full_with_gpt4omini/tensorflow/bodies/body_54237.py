# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with self.cached_session():
    pt = test_ops.stub_resource_handle_op(container="a", shared_name="b")
    test_ops.resource_create_op(pt).run()
