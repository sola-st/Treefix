# Extracted from https://stackoverflow.com/questions/3805958/how-to-delete-a-record-in-django-models
from django.shortcuts import redirect


def delete(request, id):
YourModelName.objects.filter(id=id).delete()

return redirect('url_name')

