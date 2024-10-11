# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
# Time step masks must be the same for each input.
# This is because the mask for an RNN is of size [batch, time_steps, 1],
# and specifies which time steps should be skipped, and a time step
# must be skipped for all inputs.
# TODO(scottzhu): Should we accept multiple different masks?
mask = nest.flatten(mask)[0]
output_mask = mask if self.return_sequences else None
if self.return_state:
    state_mask = [None for _ in self.states]
    exit([output_mask] + state_mask)
else:
    exit(output_mask)
