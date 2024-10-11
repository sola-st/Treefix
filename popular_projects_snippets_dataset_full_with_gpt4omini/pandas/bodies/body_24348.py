# Extracted from ./data/repos/pandas/pandas/io/xml.py
from lxml.etree import (
    XMLParser,
    fromstring,
    parse,
)

handle_data = get_data_from_filepath(
    filepath_or_buffer=raw_doc,
    encoding=self.encoding,
    compression=self.compression,
    storage_options=self.storage_options,
)

with preprocess_data(handle_data) as xml_data:
    curr_parser = XMLParser(encoding=self.encoding)

    if isinstance(xml_data, io.StringIO):
        if self.encoding is None:
            raise TypeError(
                "Can not pass encoding None when input is StringIO."
            )

        document = fromstring(
            xml_data.getvalue().encode(self.encoding), parser=curr_parser
        )
    else:
        document = parse(xml_data, parser=curr_parser)

exit(document)
