from django.views.generic import CreateView
from .forms import AnswerForm


class IndexTemplateView(CreateView):
    template_name = 'question/index.html'
    form_class = AnswerForm
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super(IndexTemplateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

