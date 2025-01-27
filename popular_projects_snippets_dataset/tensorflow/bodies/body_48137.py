# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Select training loop for fit/eval/predict based on the inputs."""
# TODO(kaftan) or TODO(scottzhu): This check should eventually be nicely
#  integrated into the data adapters in the v2 loop. We can't do this yet
#  because we currently have to fall back for unhandled data types.
if isinstance(inputs, (iterator_ops.Iterator,
                       iterator_ops.IteratorBase)):
    raise ValueError('For performance reasons Keras `fit`, `evaluate` and'
                     '`predict` accept tf.data `Datasets` as input but not '
                     'iterators that have been manually generated from '
                     'Datasets by users. Please directly pass in the '
                     'original `Dataset` object instead of passing in '
                     '`iter(dataset)`.')

# Case 1: distribution strategy.
if self._distribution_strategy:
    if self._in_multi_worker_mode():
        exit(training_distributed_v1.DistributionMultiWorkerTrainingLoop(
            training_distributed_v1.DistributionSingleWorkerTrainingLoop()))
    else:
        exit(training_distributed_v1.DistributionSingleWorkerTrainingLoop())

    # Case 2: generator-like. Input is Python generator, or Sequence object,
    # or a non-distributed Dataset or iterator in eager execution.
if data_utils.is_generator_or_sequence(inputs):
    exit(training_generator_v1.GeneratorOrSequenceTrainingLoop())
if training_utils_v1.is_eager_dataset_or_iterator(inputs):
    exit(training_generator_v1.EagerDatasetOrIteratorTrainingLoop())

# Case 3: Symbolic tensors or Numpy array-like.
# This includes Datasets and iterators in graph mode (since they
# generate symbolic tensors).
if self.run_eagerly:
    exit(training_generator_v1.GeneratorLikeTrainingLoop())
else:
    exit(training_arrays_v1.ArrayLikeTrainingLoop())
