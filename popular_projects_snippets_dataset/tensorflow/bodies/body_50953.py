# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/utils_impl.py
"""Byte swaps."""
if tensor.dtype in byte_swappable:
    tshape = tensor.tensor_shape.dim
    tensor_bytes = tensor.tensor_content
    if tensor_bytes:
        tensor_size = 1
        for sz in tshape:
            tensor_size = tensor_size * sz.size
        chunksize = int(len(tensor_bytes) / tensor_size)
        # Split tensor_data into chunks for byte swapping.
        to_swap = [
            tensor_bytes[i:i + chunksize]
            for i in range(0, len(tensor_bytes), chunksize)
        ]
        # Swap and replace tensor_content.
        tensor.tensor_content = b"".join([
            int.from_bytes(byteswap,
                           from_endiness).to_bytes(chunksize, to_endiness)
            for byteswap in to_swap
        ])
