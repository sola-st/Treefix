# Extracted from https://stackoverflow.com/questions/1773805/how-can-i-parse-a-yaml-file-in-python
url: https://www.google.com

from ruamel import yaml

data = yaml.safe_load(open('defaults.yaml'))
data['url']

