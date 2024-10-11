# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/optimize/calibrator.py
"""Feed tensors to the calibrator."""
initialized = {}

for sample in dataset_gen():
    if isinstance(sample, tuple):
        if not isinstance(sample[1], dict):
            raise ValueError("You need to provide either a dictionary with input "
                             "names and values in the second arugment in the "
                             "tuple")
        # Convert signature based inputs to the tensor index based data.
        if self._interpreter is None:
            self._interpreter = Interpreter(model_content=self._model_content)
        signature_key = sample[0]
        input_array = self._create_input_array_from_dict(
            signature_key, sample[1])
    elif isinstance(sample, dict):
        # Convert signature based inputs to the tensor index based data.
        if self._interpreter is None:
            self._interpreter = Interpreter(model_content=self._model_content)
        signature_key = None
        input_array = self._create_input_array_from_dict(None, sample)
    elif isinstance(sample, list):
        signature_key = None
        input_array = sample
    else:
        raise ValueError("You need to provide either a dictionary with input "
                         "names and values, a tuple with signature key and a "
                         "dictionary with input names and values, or an array "
                         "with input values in the order of input tensors of "
                         "the graph in the representative_dataset function. "
                         "Unsupported value from dataset: {}.".format(sample))

    if signature_key not in initialized:
        initialized[signature_key] = True
        if resize_input:
            if signature_key is not None:
                self._calibrator.Prepare([list(s.shape) for s in input_array],
                                         signature_key)
            else:
                self._calibrator.Prepare([list(s.shape) for s in input_array])
        else:
            if signature_key is not None:
                self._calibrator.Prepare(signature_key)
            else:
                self._calibrator.Prepare()
    if signature_key is not None:
        self._calibrator.FeedTensor(input_array, signature_key)
    else:
        self._calibrator.FeedTensor(input_array)
