menu = {
    'Все результаты': 'results',
    'Минимальные': 'results_min',
    'Максимальные': 'results_max',
    'Последние 100': 'results_last_100',
    'Последние 100 min': 'results_last_100_min',
    'Последние 100 max': 'results_last_100_max'
}


class ServerMixin:
    def add_range(self, context):
        gen = range(5)
        context['gen'] = gen
        context['menu'] = menu

        return context
