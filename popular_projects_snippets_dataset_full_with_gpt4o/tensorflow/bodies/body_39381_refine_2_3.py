import logging # pragma: no cover

checkpoint_dir = '/path/to/checkpoints' # pragma: no cover
latest_filename = 'checkpoint' # pragma: no cover
def get_checkpoint_state(checkpoint_dir, latest_filename=None):# pragma: no cover
    return CheckpointState(checkpoint_dir, latest_filename) # pragma: no cover
def _prefix_to_checkpoint_path(prefix, format_version):# pragma: no cover
    return prefix + f'_{format_version}' # pragma: no cover
saver_pb2 = type('Mock', (object,), {'SaverDef': type('MockSaverDef', (object,), {'V2': 'v2', 'V1': 'v1'})()}) # pragma: no cover
def file_io_get_matching_files(path):# pragma: no cover
    return [path]# pragma: no cover
def logging_error(msg, *args):# pragma: no cover
    print(msg % args)# pragma: no cover
logging.error = logging_error # pragma: no cover

import os # pragma: no cover
import logging # pragma: no cover

checkpoint_dir = '/path/to/checkpoints' # pragma: no cover
latest_filename = 'checkpoint' # pragma: no cover
def get_checkpoint_state(checkpoint_dir, latest_filename=None):# pragma: no cover
    class MockCheckpointState:# pragma: no cover
        def __init__(self):# pragma: no cover
            self.model_checkpoint_path = os.path.join(checkpoint_dir, 'mock.ckpt')# pragma: no cover
    return MockCheckpointState() # pragma: no cover
def _prefix_to_checkpoint_path(prefix, format_version):# pragma: no cover
    return prefix + f'_{format_version}' # pragma: no cover
saver_pb2 = type('Mock', (object,), {'SaverDef': type('MockSaverDef', (object,), {'V2': 'v2', 'V1': 'v1'})()}) # pragma: no cover
def file_io_get_matching_files(path):# pragma: no cover
    return [path] if os.path.exists(path) else []# pragma: no cover
file_io = type('Mock', (object,), {'get_matching_files': file_io_get_matching_files}) # pragma: no cover
def logging_error(msg, *args):# pragma: no cover
    print('ERROR:', msg % args)# pragma: no cover
logging = type('Mock', (object,), {'error': logging_error}) # pragma: no cover

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
