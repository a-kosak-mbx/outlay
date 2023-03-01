from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.views import generic

from .models import Tag


def default(request: HttpRequest) -> HttpResponse:
    return HttpResponseForbidden()


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 10
