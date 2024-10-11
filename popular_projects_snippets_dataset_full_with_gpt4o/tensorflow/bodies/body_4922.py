# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/single_loss_example.py
# input shape is [16, 8], input values are increasing in both dimensions.
exit(dataset_ops.Dataset.from_tensor_slices(
    [[[float(x * 8 + y + z * 100)
       for y in range(8)]
      for x in range(16)]
     for z in range(batch_per_epoch)]).repeat())
