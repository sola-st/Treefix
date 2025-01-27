# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/memory_optimizer_test.py
"""Tests that graph output is not significantly different with rewriting."""
(original_metagraph, init_op_name, train_op_name, loss_op_name
) = self._GetMetaGraph()
original_loss = self._RunMetaGraphWithConfig(
    config=config_pb2.ConfigProto(),
    metagraph=original_metagraph,
    init_op_name=init_op_name,
    train_op_name=train_op_name,
    loss_op_name=loss_op_name)
memory_optimized_loss = self._RunMetaGraphWithConfig(
    config=self._GetMemoryOptimizerSessionConfig(),
    metagraph=original_metagraph,
    init_op_name=init_op_name,
    train_op_name=train_op_name,
    loss_op_name=loss_op_name)
self.assertAllClose(original_loss, memory_optimized_loss, rtol=1e-2)
