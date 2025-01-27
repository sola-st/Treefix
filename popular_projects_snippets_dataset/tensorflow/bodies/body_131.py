# Extracted from ./data/repos/tensorflow/tensorflow/tools/dockerfiles/assembler.py
# See http://docs.python-cerberus.org/en/stable/customize.html
if 'partials' in kwargs:
    self.partials = kwargs['partials']
super(cerberus.Validator, self).__init__(*args, **kwargs)
