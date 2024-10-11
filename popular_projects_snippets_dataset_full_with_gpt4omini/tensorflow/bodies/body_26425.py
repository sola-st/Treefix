# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/data_service_ops.py
"""Constructs a CrossTrainerCache.

    Args:
      trainer_id: Each training job has a unique ID. Once a job has consumed
      data, the data remains in the cache and is re-used by jobs with different
      `trainer_id`s. Requests with the same `trainer_id` do not re-use data.

    Raises:
      ValueError if `trainer_id` is empty.
    """
if not trainer_id:
    raise ValueError(
        "tf.data service cross-trainer cache requires a non-empty trainer ID."
    )
self.trainer_id = trainer_id
