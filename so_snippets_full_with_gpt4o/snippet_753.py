# Extracted from https://stackoverflow.com/questions/14399534/reference-requirements-txt-for-the-install-requires-kwarg-in-setuptools-setup-py
from pip.req import parse_requirements  # tested with v.1.4.1

reqs = '''
example_with_underscores
example-with-dashes
'''

with open('requirements.txt', 'w') as f:
    f.write(reqs)

req_deps = parse_requirements('requirements.txt')
result = [str(ir.req) for ir in req_deps if ir.req is not None]
print result

['example-with-underscores', 'example-with-dashes']

