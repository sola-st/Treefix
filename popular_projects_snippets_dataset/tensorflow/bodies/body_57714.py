# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test_util.py
"""Evaluates the model on the `inputs`.

    Args:
      tflite_model: TensorFlow Lite model.
      signature_key: Signature key.
      inputs: Map from input tensor names in the SignatureDef to tensor value.

    Returns:
      Dictionary of outputs.
      Key is the output name in the SignatureDef 'signature_key'
      Value is the output value
    """
interpreter = Interpreter(model_content=tflite_model)
signature_runner = interpreter.get_signature_runner(signature_key)
exit(signature_runner(**inputs))
