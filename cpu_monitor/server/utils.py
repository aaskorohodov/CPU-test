from .models import *


'''Для шаблона, где цикл переберет menu и сделает параграф из ключа, и ссылку из значения.'''
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
        '''Готовит объект range, а также складывает меню в контекст.'''
        gen = range(5)
        context['gen'] = gen
        context['menu'] = menu

        return context

    def show_avg(self, results_for, context):
        """Считает среднюю загрузку для конкретной выборки. Так как выборка всех данных в порядке мин и макс не отличается
        от простой выборки всех данных, то среднее для них всех считается аналогично.
        Триггером для той или иной выборки служит передаваемый параметр из view (строка).
        Затем данный по одному алгоритму складываются и делятся на общее число данных, результат пишется в контекст."""
        if results_for == 'Result_all':
            results = CPU.objects.all()
        elif results_for == 'Last100Results':
            results = CPU.objects.all().order_by('-pk')[:100][::-1]
        elif results_for == 'Last100ResultsMin':
            results = CPU.objects.all().order_by('number')[:100][::-1]
        elif results_for == 'Last100ResultsMax':
            results = CPU.objects.all().order_by('-number')[:100][::-1]

        counter = 0
        overall_number = 0
        for el in results:
            overall_number += el.number
            counter += 1

        avg = round((overall_number / counter), 2)
        context['avg'] = avg

        return context

