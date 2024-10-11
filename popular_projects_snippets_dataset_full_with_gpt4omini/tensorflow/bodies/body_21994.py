# Extracted from ./data/repos/tensorflow/tensorflow/python/training/warm_starting_util_test.py
prev_vocab_path = self._write_vocab(["apple", "banana", "guava", "orange"],
                                    "old_vocab")
self._create_prev_run_var(
    "fruit_weights", initializer=[[0.5], [1.], [1.5], [2.]])

# New vocab with elements in reverse order and one new element.
new_vocab_path = self._write_vocab(
    ["orange", "guava", "banana", "apple", "raspberry"], "new_vocab")
# New session and new graph.
with ops.Graph().as_default() as g:
    with self.session(graph=g) as sess:
        fruit_weights = variable_scope.get_variable(
            "fruit_weights", initializer=[[0.], [0.], [0.], [0.], [0.]])
        ws_util._warm_start_var_with_vocab(fruit_weights, new_vocab_path, 5,
                                           self.get_temp_dir(), prev_vocab_path)
        self.evaluate(variables.global_variables_initializer())
        self.assertAllClose([[2.], [1.5], [1.], [0.5], [0.]],
                            fruit_weights.eval(sess))
