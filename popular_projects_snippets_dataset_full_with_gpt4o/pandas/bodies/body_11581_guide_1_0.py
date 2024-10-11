import pytest # pragma: no cover
from lxml.etree import XSLTApplyError # pragma: no cover
import pandas as pd # pragma: no cover
import tempfile # pragma: no cover

class TestModule: # pragma: no cover
    @staticmethod # pragma: no cover
    def ensure_clean(filename): # pragma: no cover
        class CleanContext: # pragma: no cover
            def __init__(self, filename): # pragma: no cover
                self.filename = filename # pragma: no cover
            def __enter__(self): # pragma: no cover
                open(self.filename, 'a').close()  # Create the file # pragma: no cover
                return self.filename # pragma: no cover
            def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
                os.remove(self.filename) # pragma: no cover
        return CleanContext(filename) # pragma: no cover
tm = TestModule() # pragma: no cover
geom_df = pd.DataFrame({'geometry': ['POINT (1 1)', 'POINT (2 2)']}) # pragma: no cover
def to_xml(self, path, stylesheet=None): # pragma: no cover
    root = etree.Element('root') # pragma: no cover
    for _, row in self.iterrows(): # pragma: no cover
        geom_elem = etree.SubElement(root, 'geometry') # pragma: no cover
        geom_elem.text = row['geometry'] # pragma: no cover
    doc = etree.ElementTree(root) # pragma: no cover
    if stylesheet: # pragma: no cover
        xslt_root = etree.XML(stylesheet) # pragma: no cover
        transform = etree.XSLT(xslt_root) # pragma: no cover
        doc = transform(doc) # pragma: no cover
    with open(path, 'wb') as xml_file: # pragma: no cover
        xml_file.write(etree.tostring(doc, pretty_print=True, xml_declaration=True, encoding='UTF-8')) # pragma: no cover
pd.DataFrame.to_xml = to_xml # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
from l3.Runtime import _l_
try:
    from lxml.etree import XSLTApplyError
    _l_(21714)

except ImportError:
    pass

xsl = """\
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="xml" encoding="utf-8" indent="yes" />
    <xsl:strip-space elements="*"/>

    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:copy-of select="document('non_existent.xml')/*"/>
        </xsl:copy>
    </xsl:template>
</xsl:stylesheet>"""
_l_(21715)

with pytest.raises(XSLTApplyError, match=("Cannot resolve URI")):
    _l_(21718)

    with tm.ensure_clean("test.xml") as path:
        _l_(21717)

        geom_df.to_xml(path, stylesheet=xsl)
        _l_(21716)
