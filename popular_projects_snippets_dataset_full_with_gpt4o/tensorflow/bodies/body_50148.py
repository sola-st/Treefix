# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/utils_v1/export_utils.py
"""Log a report of which signatures were produced."""
sig_names_by_method_name = collections.defaultdict(list)

# We'll collect whatever method_names are present, but also we want to make
# sure to output a line for each of the three standard methods even if they
# have no signatures.
for method_name in _FRIENDLY_METHOD_NAMES:
    sig_names_by_method_name[method_name] = []

for signature_name, sig in signature_def_map.items():
    sig_names_by_method_name[sig.method_name].append(signature_name)

# TODO(b/67733540): consider printing the full signatures, not just names
for method_name, sig_names in sig_names_by_method_name.items():
    if method_name in _FRIENDLY_METHOD_NAMES:
        method_name = _FRIENDLY_METHOD_NAMES[method_name]
    logging.info('Signatures INCLUDED in export for {}: {}'.format(
        method_name, sig_names if sig_names else 'None'))

if excluded_signatures:
    logging.info('Signatures EXCLUDED from export because they cannot be '
                 'be served via TensorFlow Serving APIs:')
    for signature_name, message in excluded_signatures.items():
        logging.info('\'{}\' : {}'.format(signature_name, message))

if not signature_def_map:
    logging.warning('Export includes no signatures!')
elif (signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY not in
      signature_def_map):
    logging.warning('Export includes no default signature!')
