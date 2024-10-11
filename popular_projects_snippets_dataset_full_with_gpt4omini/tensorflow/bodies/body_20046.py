# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""Creates op for enqueuing batch to TPU."""
enqueue_data0 = list(enqueue_datas.values())[0]
with ops.colocate_with(enqueue_data0.embedding_indices):
    exit(tpu_ops.enqueue_tpu_embedding_arbitrary_tensor_batch(
        device_ordinal=device_ordinal,
        combiners=self._combiners,
        mode_override=mode_override,
        **self._format_for_tpu_embedding_arbitrary_tensor_batch(
            enqueue_datas, ragged)))
