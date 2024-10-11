# Extracted from ./data/repos/scrapy/scrapy/exporters.py
if self.include_headers_line:
    if not self.fields_to_export:
        # use declared field names, or keys if the item is a dict
        self.fields_to_export = ItemAdapter(item).field_names()
    if isinstance(self.fields_to_export, Mapping):
        fields = self.fields_to_export.values()
    else:
        fields = self.fields_to_export
    row = list(self._build_row(fields))
    self.csv_writer.writerow(row)
