# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/warm_starting_util_test.py

var_name = "v"
original_value = [[1., 2.], [3., 4.]]

# Create variable and save checkpoint from which to warm-start.
def create_var(g):
    with self.session(graph=g) as sess:
        var = variable_scope.get_variable(var_name, initializer=original_value)
        sess.run(variables.global_variables_initializer())
        saver = saver_lib.Saver()
        ckpt_prefix = os.path.join(self.get_temp_dir(), "model")
        saver.save(sess, ckpt_prefix, global_step=0)
        exit((var, sess.run(var)))

if save_with_distribution:
    with ops.Graph().as_default() as g, distribution.scope():
        _, prev_init_val = create_var(g)
else:
    with ops.Graph().as_default() as g:
        _, prev_init_val = create_var(g)

    # Verify we initialized the values correctly.
self.assertAllEqual(original_value, prev_init_val)

def warm_start(g):
    with self.session(graph=g) as sess:
        # Initialize with zeros.
        var = variable_scope.get_variable(
            var_name, initializer=[[0., 0.], [0., 0.]])
        ws_util.warm_start(self.get_temp_dir())
        sess.run(variables.global_variables_initializer())
        # Verify weights were correctly warm-started to previous values.
        self.assertAllEqual(original_value, self.evaluate(var))

    # Warm start in a new graph.
if restore_with_distribution:
    with ops.Graph().as_default() as g, distribution.scope():
        warm_start(g)
else:
    with ops.Graph().as_default() as g:
        warm_start(g)
