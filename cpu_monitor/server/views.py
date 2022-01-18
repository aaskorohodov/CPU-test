from django.http import HttpResponse
from django.views.generic import DetailView, TemplateView, ListView

from .models import *
from .utils import *


def cpu_server(request, cpu):
    """Обрабатывает запрос на сохранение конкретного измерения загрузки CPU. Не рисует страницу, дает код ответа.
    cpu = захваченный слаг из url
    item = экземпляр модели, в которую запишем измерение
    Предварительно слаг превращается во float, земля_ заменяется на точку."""
    cpu = float(cpu.replace('_', '.'))
    item = CPU()
    item.number = cpu
    item.save()
    return HttpResponse()


class Result(ServerMixin, ListView):
    """Рисует главную страницу с результатами. Наследуется от миксина ServerMixin, который добавляет в контекст
    меню (для шаблона) и возвращает объект range, для его перебора в шаблоне, с целью отрисовать N заголовков (5).
    Range используется, чтобы сократить размер шаблона, сделав цикл.
    Прочие классы ниже аналогичны, отвечают за отрисовку филтрованных данных. Отличаются наличием метода get_queryset,
    который и делает нужную выборку."""

    model = CPU
    template_name = 'server.html'
    context_object_name = 'cpus'
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Два вызова для наглядности (смотрите: сначала сделали это, результат сложили туда, затем то, результат тут)
        context = self.add_range(context)
        context = self.show_avg('Result_all', context)

        return context


class ResultMin(ServerMixin, ListView):
    model = CPU
    template_name = 'server.html'
    context_object_name = 'cpus'
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = self.add_range(context)
        context = self.show_avg('Result_all', context)

        return context

    def get_queryset(self, **kwargs):
        return CPU.objects.all().order_by('number')


class ResultMax(ServerMixin, ListView):
    model = CPU
    template_name = 'server.html'
    context_object_name = 'cpus'
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = self.add_range(context)
        context = self.show_avg('Result_all', context)

        return context

    def get_queryset(self, **kwargs):
        return CPU.objects.all().order_by('-number')


class Last100Results(ServerMixin, ListView):
    model = CPU
    template_name = 'server.html'
    context_object_name = 'cpus'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = self.add_range(context)
        context = self.show_avg('Last100Results', context)

        return context

    def get_queryset(self, **kwargs):
        '''Выстраиваем обратный порядок по pk, берем последние 100 записей, переворачиваем записи.'''
        return CPU.objects.all().order_by('-pk')[:100][::-1]


class Last100ResultsMin(ServerMixin, ListView):
    model = CPU
    template_name = 'server.html'
    context_object_name = 'cpus'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = self.add_range(context)
        context = self.show_avg('Last100ResultsMin', context)

        return context

    def get_queryset(self, **kwargs):
        return CPU.objects.all().order_by('number')[:100][::-1]


class Last100ResultsMax(ServerMixin, ListView):
    model = CPU
    template_name = 'server.html'
    context_object_name = 'cpus'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = self.add_range(context)
        context = self.show_avg('Last100ResultsMax', context)

        return context

    def get_queryset(self, **kwargs):
        return CPU.objects.all().order_by('-number')[:100][::-1]