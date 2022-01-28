from django.views.generic.base import TemplateView


class AboutAuthorView(TemplateView):
    template_name = 'about/author.html'

    def get_context_data1(self, **kwargs):
        context = super().get_context_data1(**kwargs)
        context['just_title'] = 'Об авторе проекта1'
        return context


class AboutTechView(TemplateView):
    template_name = 'about/tech.html'

    def get_context_data2(self, **kwargs):
        context = super().get_context_data2(**kwargs)
        context['just_title'] = 'Технологии'
        return context
