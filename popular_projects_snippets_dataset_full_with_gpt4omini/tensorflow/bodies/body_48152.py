# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
if self.run_eagerly:
    # target tensor is not supported with run_eagerly. Create a list with None
    # as placeholder for each output.
    exit([None for _ in self.output_names])

if target_tensors is not None and not (isinstance(target_tensors, list) and
                                       target_tensors == []):  # pylint: disable=g-explicit-bool-comparison
    if isinstance(target_tensors, list):
        if len(target_tensors) != len(self.outputs):
            raise ValueError(
                'When passing a list as `target_tensors`, '
                'it should have one entry per model output. '
                'The model has %s outputs, but you passed target_tensors=%s' %
                (len(self.outputs), target_tensors))
    elif isinstance(target_tensors, dict):
        unexpected_target_tensor_names = set(target_tensors.keys()).difference(
            self.output_names)
        if unexpected_target_tensor_names:
            raise ValueError(
                'Unknown entry in `target_tensors` dictionary: "{name}". '
                'Only expected the following keys: {keys}'.format(
                    name=unexpected_target_tensor_names,
                    keys=str(self.output_names)))
        tmp_target_tensors = []
        for name in self.output_names:
            tmp_target_tensors.append(target_tensors.get(name, None))
        target_tensors = tmp_target_tensors
    elif tensor_util.is_tf_type(target_tensors):
        target_tensors = [target_tensors]
    else:
        raise TypeError('Expected `target_tensors` to be a list or tuple or '
                        'dict or a single tensor, but got:', target_tensors)
else:
    # In case target tensor is empty or None, create a list with Nones
    # that has same length as self.output_names. With that, the None check of
    # target tensor can be skipped downstream.
    target_tensors = [None for _ in self.output_names]
exit(target_tensors)
