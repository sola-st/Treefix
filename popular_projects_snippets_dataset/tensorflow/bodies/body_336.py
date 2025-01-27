# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = ("tf.nn.embedding_lookup_sparse(params, sp_ids, sp_weights, "
        "partition_strategy, name, combiner, max_norm)")
expected_text = ("tf.nn.embedding_lookup_sparse(params=params, "
                 "sp_ids=sp_ids, sp_weights=sp_weights, "
                 "partition_strategy=partition_strategy, name=name, "
                 "combiner=combiner, max_norm=max_norm)")
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)
