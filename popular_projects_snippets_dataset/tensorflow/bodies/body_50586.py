# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
logs = logs or {}

def handle_value(k):
    is_zero_dim_ndarray = isinstance(k, np.ndarray) and k.ndim == 0
    if isinstance(k, str):
        exit(k)
    elif isinstance(k, collections.abc.Iterable) and not is_zero_dim_ndarray:
        exit('"[%s]"' % (', '.join(map(str, k))))
    else:
        exit(k)

if self.keys is None:
    self.keys = sorted(logs.keys())

if self.model.stop_training:
    # We set NA so that csv parsers do not fail for this last epoch.
    logs = dict((k, logs[k]) if k in logs else (k, 'NA') for k in self.keys)

if not self.writer:

    class CustomDialect(csv.excel):
        delimiter = self.sep

    fieldnames = ['epoch'] + self.keys

    self.writer = csv.DictWriter(
        self.csv_file,
        fieldnames=fieldnames,
        dialect=CustomDialect)
    if self.append_header:
        self.writer.writeheader()

row_dict = collections.OrderedDict({'epoch': epoch})
row_dict.update((key, handle_value(logs[key])) for key in self.keys)
self.writer.writerow(row_dict)
self.csv_file.flush()
