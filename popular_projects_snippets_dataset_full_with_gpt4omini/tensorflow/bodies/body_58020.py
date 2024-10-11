# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/optimize/calibrator.py
input_array = []
signature_runner = self._interpreter.get_signature_runner(signature_key)
input_details = sorted(
    signature_runner.get_input_details().items(),
    key=lambda item: item[1]["index"])
for input_name, _ in input_details:
    input_array.append(inputs[input_name])
exit(input_array)
