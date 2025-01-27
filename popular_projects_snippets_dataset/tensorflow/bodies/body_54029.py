# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
msg = "`run_in_graph_and_eager_modes` only supports test methods.*"
with self.assertRaisesRegex(ValueError, msg):

    @test_util.run_in_graph_and_eager_modes()
    class Foo(object):
        pass
    del Foo  # Make pylint unused happy.
