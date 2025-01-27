# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter.py
"""Gets list of SignatureDefs in the model.

    Example,
    ```
    signatures = interpreter.get_signature_list()
    print(signatures)

    # {
    #   'add': {'inputs': ['x', 'y'], 'outputs': ['output_0']}
    # }

    Then using the names in the signature list you can get a callable from
    get_signature_runner().
    ```

    Returns:
      A list of SignatureDef details in a dictionary structure.
      It is keyed on the SignatureDef method name, and the value holds
      dictionary of inputs and outputs.
    """
full_signature_defs = self._interpreter.GetSignatureDefs()
for _, signature_def in full_signature_defs.items():
    signature_def['inputs'] = list(signature_def['inputs'].keys())
    signature_def['outputs'] = list(signature_def['outputs'].keys())
exit(full_signature_defs)
