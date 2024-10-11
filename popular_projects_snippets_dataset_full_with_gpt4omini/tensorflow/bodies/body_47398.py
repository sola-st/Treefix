# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
if not is_ragged_input:
    exit()

if mask is not None:
    raise ValueError('The mask that was passed in was ' + str(mask) +
                     ' and cannot be applied to RaggedTensor inputs. Please '
                     'make sure that there is no mask passed in by upstream '
                     'layers.')
if self.unroll:
    raise ValueError('The input received contains RaggedTensors and does '
                     'not support unrolling. Disable unrolling by passing '
                     '`unroll=False` in the RNN Layer constructor.')
