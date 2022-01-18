from django.http import HttpResponse
from django.views.generic import DetailView, TemplateView, ListView

from .models import *
from .utils import *


def cpu_server(request, cpu):
    cpu = float(cpu.replace('_', '.'))
    item = CPU()
    item.number = cpu
    item.save()
    return HttpResponse()


class Result(ServerMixin, ListView):
    model = CPU
    template_name = 'server.html'
    context_object_name = 'cpus'
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = self.add_range(context)

        return context


class ResultMin(ServerMixin, ListView):
    model = CPU
    template_name = 'server.html'
    context_object_name = 'cpus'
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = self.add_range(context)

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

        return context

    def get_queryset(self, **kwargs):
        return CPU.objects.all().order_by('-pk')[:100][::-1]


class Last100ResultsMin(ServerMixin, ListView):
    model = CPU
    template_name = 'server.html'
    context_object_name = 'cpus'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = self.add_range(context)

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

        return context

    def get_queryset(self, **kwargs):
        return CPU.objects.all().order_by('-number')[:100][::-1]