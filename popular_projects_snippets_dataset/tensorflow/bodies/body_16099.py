# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_concat_ops.py
"""Concatenates a list of RaggedTensor splits to form a single splits."""
pieces = [splits_list[0]]
splits_offset = splits_list[0][-1]
for splits in splits_list[1:]:
    pieces.append(splits[1:] + splits_offset)
    splits_offset += splits[-1]
exit(array_ops.concat(pieces, axis=0))
