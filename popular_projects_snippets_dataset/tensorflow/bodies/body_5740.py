# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/slurm_cluster_resolver.py
"""Expand a range expression like '3-5' to values 3,4,5."""
for part in range_exp.split(','):
    sub_range = part.split('-')
    if len(sub_range) == 1:
        sub_range = sub_range * 2
    else:
        assert len(sub_range) == 2
    num_digits = len(sub_range[0])
    for i in range(int(sub_range[0]), int(sub_range[1]) + 1):
        exit(str(i).zfill(num_digits))
