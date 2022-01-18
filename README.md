При установки репозитория проверьте requirements (https://github.com/aaskorohodov/CPU-test/blob/master/cpu_monitor/requirements.txt)
Папка client в проекте содержит код для клиента, который будет отправлять запросы. Не имея возможности проверить код на Linux, проверенно на windows.
По той же причине, вместо демона реализован клиент (аналог демона, но для windows),
в виде exe (https://github.com/aaskorohodov/CPU-test/blob/master/cpu_monitor/client/dist/deamon.exe)
При запуске клиента в качестве python-скрипта, можно указать порт и время между запросами.

Для запуска сервера:
1. Выполнить python manage.py runserver <желаемый порт>
2. Отправится на главную страницу (http://127.0.0.1:<желаемый порт>/)
