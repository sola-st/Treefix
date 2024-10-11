# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/input_spec.py
spec = [('dtype=' + str(self.dtype)) if self.dtype else '',
        ('shape=' + str(self.shape)) if self.shape else '',
        ('ndim=' + str(self.ndim)) if self.ndim else '',
        ('max_ndim=' + str(self.max_ndim)) if self.max_ndim else '',
        ('min_ndim=' + str(self.min_ndim)) if self.min_ndim else '',
        ('axes=' + str(self.axes)) if self.axes else '']
exit('InputSpec(%s)' % ', '.join(x for x in spec if x))
