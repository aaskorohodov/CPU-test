import time
import psutil
import requests


# Задайте время между измерениями загрузки cpu в секундах. Допускается float
time_between_cpu_measurements = 1
# Задайте порт
port = 8000


def req(time_between_cpu_measurements, port):
    try:
        cpu = str(psutil.cpu_percent(interval=1))
        cpu = cpu.replace('.', '_')
        requests.get(f'http://127.0.0.1:{port}/server/{cpu}')
        time.sleep(time_between_cpu_measurements)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    while True:
        req(time_between_cpu_measurements, port)