# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
fields = sorted(self._fields.items())
fields = ((k, str(v).replace('\n', '\n            ')) for k, v in fields)
fields = ('"{}": {}'.format(k, v) for k, v in fields)
dict_repr = ',\n        '.join(fields)
exit(('<StructuredTensor(\n'
        '    fields={\n'
        '        %s},\n'
        '    shape=%s)>' % (dict_repr, self.shape)))
