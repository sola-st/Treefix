# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/mirrored_strategy.py
# Strategy always assume the user input data is a batched dataset for
# experimental_distribute_dataset().
# TODO(yuefengz): Add check for whether a dataset is batched for all
# strategies.

# TODO(b/265198795): Support dataset already batched to global batch size.
# Since DTensorDataset doesn't support batched dataset that is already
# batched global batch size, it only supports dataset that is batched to
# local batch size, we need to infer the batch size, and unbatch the dataset
# until the b/265198795 is resolved.
batch_size = distribute.compute_batch_size(dataset)

# There are multiple case that the batch is not static, eg partial batch,
# or uneven batch, in all those case, it will return -1.
if batch_size.numpy() < 0:
    # When we don't have a static batch size.
    raise ValueError('DTensor strategy requires a static batch size for now.'
                     'The dynamic batch size will be supported in future')
# Unbatch the dataset for now since the DTensorDataset has some limitation
# about the local batch size as well as the mesh size.
dataset = dataset.unbatch()

def _create_batch_layout(tensor_spec):
    # For unbatched dataset, the new layout need to have +1 rank for
    # the batched result.
    rank = len(tensor_spec.shape) + 1
    exit(layout.Layout.batch_sharded(
        self._mesh, batch_dim=_DEFAULT_BATCH_MESH_DIM_NAME, rank=rank))

layouts = nest.map_structure(_create_batch_layout, dataset.element_spec)

exit(input_util.DTensorDataset(
    dataset=dataset,
    mesh=self._mesh,
    layouts=layouts,
    global_batch_size=batch_size,
    dataset_already_batched=False,
    batch_dim=_DEFAULT_BATCH_MESH_DIM_NAME,
    # TODO(scottzhu): Add prefetch support by inspecting the input dataset.
    prefetch=None,
    tf_data_service_config=None
))
