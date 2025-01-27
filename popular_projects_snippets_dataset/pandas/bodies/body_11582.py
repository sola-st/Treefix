# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
xsl = """\
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="xml" encoding="utf-8" indent="yes" />
    <xsl:strip-space elements="*"/>

    <xsl:template match="@*|node(*)">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>"""

with pytest.raises(
    ValueError, match=("To use stylesheet, you need lxml installed")
):
    geom_df.to_xml(parser="etree", stylesheet=xsl)
