# Extracted from https://stackoverflow.com/questions/1465249/get-lengths-of-a-list-in-a-jinja2-template
{% for i in range(0,(nums['list_users_response']['list_users_result']['users'])| length) %}
{% endfor %}

