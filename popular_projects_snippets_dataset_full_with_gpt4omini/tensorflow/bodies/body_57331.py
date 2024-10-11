# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter.py
"""Constructor.

    Args:
      interpreter: Interpreter object that is already initialized with the
        requested model.
      signature_key: SignatureDef key to be used.
    """
if not interpreter:
    raise ValueError('None interpreter provided.')
if not signature_key:
    raise ValueError('None signature_key provided.')
self._interpreter = interpreter
self._interpreter_wrapper = interpreter._interpreter
self._signature_key = signature_key
signature_defs = interpreter._get_full_signature_list()
if signature_key not in signature_defs:
    raise ValueError('Invalid signature_key provided.')
self._signature_def = signature_defs[signature_key]
self._outputs = self._signature_def['outputs'].items()
self._inputs = self._signature_def['inputs']

self._subgraph_index = (
    self._interpreter_wrapper.GetSubgraphIndexFromSignature(
        self._signature_key))
