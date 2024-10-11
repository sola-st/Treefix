# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/async_checkpoint_test.py
labels = math_ops.cast(labels, dtypes.int64)
logging.info('LABELS %s %s', labels, logits)
exit({
    'recall@1': metrics_lib.recall_at_k(labels, logits, 1),
    'recall@5': metrics_lib.recall_at_k(labels, logits, 5),
})
