from typing import Any, Dict
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import BoardForm
from bboard.models import Board, Rubrick


def main_title(request):
    template = loader.get_template("base.html")
    rubrics = Rubrick.objects.all()
    context = {
        "rubrics": rubrics,
            }
    return HttpResponse(template.render(request=request, context=context))


def index(request):
    bbs = Board.objects.order_by('-published')
    rubrics = Rubrick.objects.all()
    context = {
        "bbs": bbs,
        "rubrics": rubrics,
            }
    return render(request, "board/index.html", context=context)


def by_rubric(request, rubric_id):
    bbs = Board.objects.filter(rubric=rubric_id)
    rubrics = Rubrick.objects.all()
    current_rubric = Rubrick.objects.get(pk=rubric_id)
    
    context = {'bbs': bbs,
               "rubrics": rubrics,
               "current_rubric": current_rubric,
                }
    return  render(request, template_name='board/by_rubric.html', context=context)


class BoardCreateView(CreateView):
    template_name = "board/create.html"
    form_class = BoardForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubrick.objects.all()
        return context
