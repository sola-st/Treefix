# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/generate2.py
content = yaml.safe_load(path.read_text())
exit(content)

with path.open("w") as f:
    yaml.dump(content, f, default_flow_style=False)
