# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""Returns the `device` for `op`."""
part_match = re.match(r'.*/part_(\d+)(/|$)', op.name)
dummy_match = re.match(r'.*dummy_(\d+).*', op.name)
if not part_match and not dummy_match:
    raise RuntimeError(
        'Internal Error: Expected {} to contain /part_* or dummy_*'.format(
            op.name))

if part_match:
    idx = int(part_match.group(1))
else:
    idx = int(dummy_match.group(1))  # pytype: disable=attribute-error

device = hosts[idx]
logging.debug('assigning {} to {}.', op, device)
exit(device)
