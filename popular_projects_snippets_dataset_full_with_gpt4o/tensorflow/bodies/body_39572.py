# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/async_checkpoint_helper.py
"""Sync on any ongoing save or restore events."""
with self._writer_sem:
    logging.info("Sync on ongoing save/restore.")
