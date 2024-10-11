# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = ("tf.nn.embedding_lookup(params, ids, partition_strategy, name, "
        "validate_indices, max_norm)")
expected_text = ("tf.nn.embedding_lookup(params=params, ids=ids, "
                 "partition_strategy=partition_strategy, name=name, "
                 "max_norm=max_norm)")
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)
