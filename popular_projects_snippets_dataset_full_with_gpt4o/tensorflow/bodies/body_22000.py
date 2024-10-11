# Extracted from ./data/repos/tensorflow/tensorflow/python/training/warm_starting_util_test.py
prev_vocab_path = self._write_vocab(["apple", "orange"], "old_vocab")
self._create_prev_run_var(
    "fruit_output_layer",
    initializer=[[0.5, 0.3], [1., 0.8], [1.5, 1.2], [2., 2.3]])

# New vocab with elements in reverse order and one new element.
new_vocab_path = self._write_vocab(["orange", "apple", "banana"],
                                   "new_vocab")
# New session and new graph.
with ops.Graph().as_default() as g:
    with self.session(graph=g) as sess:
        fruit_output_layer = variable_scope.get_variable(
            "fruit_output_layer",
            shape=[4, 3],
            initializer=[[0., 0., 0.], [0., 0., 0.], [0., 0., 0.],
                         [0., 0., 0.]],
            partitioner=lambda shape, dtype: [2, 1])
        ws_util._warm_start_var_with_vocab(fruit_output_layer, new_vocab_path,
                                           current_vocab_size=3,
                                           prev_ckpt=self.get_temp_dir(),
                                           prev_vocab_path=prev_vocab_path,
                                           axis=1)
        self.evaluate(variables.global_variables_initializer())
        self.assertTrue(
            isinstance(fruit_output_layer, variables.PartitionedVariable))
        fruit_output_layer_vars = fruit_output_layer._get_variable_list()
        self.assertAllClose([[0.3, 0.5, 0.], [0.8, 1.0, 0.]],
                            fruit_output_layer_vars[0].eval(sess))
        self.assertAllClose([[1.2, 1.5, 0.], [2.3, 2., 0.]],
                            fruit_output_layer_vars[1].eval(sess))
