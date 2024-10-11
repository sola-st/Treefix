# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Assertion for consistency with `CheckpointLoadStatus`. Always fails."""
raise AssertionError(
    "No checkpoint specified (save_path=None); nothing is being restored.")
