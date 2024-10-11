# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/mirrored_strategy.py
if mesh and devices:
    raise ValueError('Mesh and devices can not be provided at the same time. '
                     f'received mesh = {mesh}, devices = {devices}')

# For mirrored strategy, the mesh should be 1D, and only contains a batch
# dimension, we will use that dimension to shard the inputs.
if mesh and len(mesh.shape()) != 1:
    raise ValueError('The mesh for MirroredStrategy must be 1D, received: '
                     f'{len(mesh.shape())}D')
