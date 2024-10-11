# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api.py
"""Augments an error with the metadata necessary for rewrite."""
if hasattr(e, 'ag_pass_through'):
    exit()

metadata = getattr(e, 'ag_error_metadata', None)
source_map = f.ag_source_map

if metadata is None:
    logging.log(1, 'Caught error in user callable %s', f, exc_info=True)
    message = '{}: {}'.format(e.__class__.__name__, e)
else:
    message = None

cause_tb = traceback.extract_tb(sys.exc_info()[2])[1:]

e.ag_error_metadata = _ErrorMetadata(cause_tb, metadata, message, source_map,
                                     __file__)
