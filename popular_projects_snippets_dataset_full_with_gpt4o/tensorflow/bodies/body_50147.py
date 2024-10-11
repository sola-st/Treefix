# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/utils_v1/export_utils.py
"""Build `SignatureDef`s for all export outputs.

  Args:
    receiver_tensors: a `Tensor`, or a dict of string to `Tensor`, specifying
      input nodes where this receiver expects to be fed by default.  Typically,
      this is a single placeholder expecting serialized `tf.Example` protos.
    export_outputs: a dict of ExportOutput instances, each of which has
      an as_signature_def instance method that will be called to retrieve
      the signature_def for all export output tensors.
    receiver_tensors_alternatives: a dict of string to additional
      groups of receiver tensors, each of which may be a `Tensor` or a dict of
      string to `Tensor`.  These named receiver tensor alternatives generate
      additional serving signatures, which may be used to feed inputs at
      different points within the input receiver subgraph.  A typical usage is
      to allow feeding raw feature `Tensor`s *downstream* of the
      tf.io.parse_example() op.  Defaults to None.
    serving_only: boolean; if true, resulting signature defs will only include
      valid serving signatures. If false, all requested signatures will be
      returned.

  Returns:
    signature_def representing all passed args.

  Raises:
    ValueError: if export_outputs is not a dict
  """
if not isinstance(receiver_tensors, dict):
    receiver_tensors = {SINGLE_RECEIVER_DEFAULT_NAME: receiver_tensors}
if export_outputs is None or not isinstance(export_outputs, dict):
    raise ValueError('export_outputs must be a dict and not'
                     '{}'.format(type(export_outputs)))

signature_def_map = {}
excluded_signatures = {}
for output_key, export_output in export_outputs.items():
    signature_name = '{}'.format(output_key or 'None')
    try:
        signature = export_output.as_signature_def(receiver_tensors)
        signature_def_map[signature_name] = signature
    except ValueError as e:
        excluded_signatures[signature_name] = str(e)

if receiver_tensors_alternatives:
    for receiver_name, receiver_tensors_alt in (
        receiver_tensors_alternatives.items()):
        if not isinstance(receiver_tensors_alt, dict):
            receiver_tensors_alt = {
                SINGLE_RECEIVER_DEFAULT_NAME: receiver_tensors_alt
            }
        for output_key, export_output in export_outputs.items():
            signature_name = '{}:{}'.format(receiver_name or 'None', output_key or
                                            'None')
            try:
                signature = export_output.as_signature_def(receiver_tensors_alt)
                signature_def_map[signature_name] = signature
            except ValueError as e:
                excluded_signatures[signature_name] = str(e)

_log_signature_report(signature_def_map, excluded_signatures)

# The above calls to export_output_lib.as_signature_def should return only
# valid signatures; if there is a validity problem, they raise a ValueError,
# in which case we exclude that signature from signature_def_map above.
# The is_valid_signature check ensures that the signatures produced are
# valid for serving, and acts as an additional sanity check for export
# signatures produced for serving. We skip this check for training and eval
# signatures, which are not intended for serving.
if serving_only:
    signature_def_map = {
        k: v
        for k, v in signature_def_map.items()
        if signature_def_utils.is_valid_signature(v)
    }
exit(signature_def_map)
