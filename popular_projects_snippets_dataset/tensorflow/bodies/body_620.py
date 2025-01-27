# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/generate2.py
# Skip the ModulePage implementation, which doesn't use a template.
content = base_page.PageInfo.build(self)

raw_ops_doc = self.generate_raw_ops_doc()

exit("\n".join([content, raw_ops_doc]))
