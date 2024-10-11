import os # pragma: no cover

checkpoint_dir = '/path/to/checkpoint_dir' # pragma: no cover
latest_filename = None # pragma: no cover
_prefix_to_checkpoint_path = lambda prefix, saver_def: f'{prefix}-{saver_def}' # pragma: no cover

import os # pragma: no cover

checkpoint_dir = '/path/to/checkpoint_dir' # pragma: no cover
latest_filename = None # pragma: no cover
get_checkpoint_state = lambda dir, latest_filename=None: type('MockCheckpointState', (object,), {'model_checkpoint_path': '/path/to/mock_checkpoint'})() # pragma: no cover
_prefix_to_checkpoint_path = lambda prefix, saver_def: f'{prefix}-{saver_def}' # pragma: no cover
file_io = type('Mock', (object,), {'get_matching_files': lambda path: [path] if os.path.exists(path) else []}) # pragma: no cover
logging = type('Mock', (object,), {'error': lambda msg, *args: print(msg % args)}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management.py
from l3.Runtime import _l_
"""Finds the filename of latest saved checkpoint file.

  Gets the checkpoint state given the provided checkpoint_dir and looks for a
  corresponding TensorFlow 2 (preferred) or TensorFlow 1.x checkpoint path.
  The latest_filename argument is only applicable if you are saving checkpoint
  using `v1.train.Saver.save`


  See the [Training Checkpoints
  Guide](https://www.tensorflow.org/guide/checkpoint) for more details and
  examples.`

  Args:
    checkpoint_dir: Directory where the variables were saved.
    latest_filename: Optional name for the protocol buffer file that
      contains the list of most recent checkpoint filenames.
      See the corresponding argument to `v1.train.Saver.save`.

  Returns:
    The full path to the latest checkpoint or `None` if no checkpoint was found.
  """
# Pick the latest checkpoint based on checkpoint state.
ckpt = get_checkpoint_state(checkpoint_dir, latest_filename)
_l_(20449)
if ckpt and ckpt.model_checkpoint_path:
    _l_(20455)

    # Look for either a V2 path or a V1 path, with priority for V2.
    v2_path = _prefix_to_checkpoint_path(ckpt.model_checkpoint_path,
                                         saver_pb2.SaverDef.V2)
    _l_(20450)
    v1_path = _prefix_to_checkpoint_path(ckpt.model_checkpoint_path,
                                         saver_pb2.SaverDef.V1)
    _l_(20451)
    if file_io.get_matching_files(v2_path) or file_io.get_matching_files(
        v1_path):
        _l_(20454)

        aux = ckpt.model_checkpoint_path
        _l_(20452)
        exit(aux)
    else:
        logging.error("Couldn't match files for checkpoint %s",
                      ckpt.model_checkpoint_path)
        _l_(20453)
aux = None
_l_(20456)
exit(aux)
