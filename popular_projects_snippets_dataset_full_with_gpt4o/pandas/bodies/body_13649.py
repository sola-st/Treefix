# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_html.py
p = tmpdir.mkdir("tpl").join("myhtml_style.tpl")
p.write(
    dedent(
        """\
            {% extends "html_style.tpl" %}
            {% block style %}
            <link rel="stylesheet" href="mystyle.css">
            {{ super() }}
            {% endblock style %}"""
    )
)
result = Styler.from_custom_template(
    str(tmpdir.join("tpl")), html_style="myhtml_style.tpl"
)
assert issubclass(result, Styler)
assert result.env is not Styler.env
assert result.template_html_style is not Styler.template_html_style
styler = result(DataFrame({"A": [1, 2]}))
assert '<link rel="stylesheet" href="mystyle.css">\n\n<style' in styler.to_html()
