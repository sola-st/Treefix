# Extracted from https://stackoverflow.com/questions/629551/how-to-query-as-group-by-in-django
from django.db.models import OuterRef, Exists

qs = Members.objects.all()
qs = qs.annotate(is_duplicate=Exists(
    Members.objects.filter(
        id__lt=OuterRef('id'),
        designation=OuterRef('designation')))
qs = qs.filter(is_duplicate=False)

