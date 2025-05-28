import random
import struct
import math

import pyaudio
import pyautogui
import time

import requests
from pynput.keyboard import Controller
from PIL import ImageGrab


def create_scr():
    img = ImageGrab.grab()
    img.save("screenshot.jpg", "jpeg")


def click_1():
    keyboard = Controller()
    keyboard.press('1')
    keyboard.release('1')
    print('Закидываем удочку...')


def click_rb():
    pyautogui.click(button='right')
    print('Подсекаем...')


def send_to_neuro():
    return requests.post('http://localhost:8000/get_coords', files={'image': open('screenshot.jpg', 'rb')}).json()


def move_to_coords(coords):
    pyautogui.moveTo(coords['x'], coords['y'], duration=random.random())


def listen():
    # Параметры аудио
    CHUNK = 1024  # Размер блока данных
    FORMAT = pyaudio.paInt16  # Формат аудио
    CHANNELS = 2  # Количество каналов
    RATE = 44100  # Частота дискретизации
    # Инициализация PyAudio
    p = pyaudio.PyAudio()
    # Открытие потока для чтения
    stream = p.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK, input_device_index=2)
    def calculate_rms(data):
        """Вычисление среднеквадратичного значения (RMS)"""
        count = len(data) // 2  # Количество отсчетов при формате int16
        format_str = "<" + "h" * count
        shorts = struct.unpack_from(format_str, data)
        sum_squares = sum(sample ** 2 for sample in shorts)
        return math.sqrt(sum_squares / count) if count > 0 else 0
    try:
        print("Ждем...")
        start = time.perf_counter()
        now = 0
        while now < 20:
            # Чтение данных из потока
            data = stream.read(CHUNK)

            # Вычисление RMS для текущего блока данных
            rms_value = calculate_rms(data)

            # Проверка на наличие звука (пороговое значение)
            if rms_value > 200:  # Пороговое значение можно настроить
                print("Бульк!")
                break
            now = time.perf_counter() - start
    except KeyboardInterrupt:
        print("Остановка по запросу пользователя.")
    finally:
        # Закрытие потока и PyAudio
        stream.stop_stream()
        stream.close()
        p.terminate()


def start_fishing():
    time.sleep(5)
    while True:
        click_1()
        time.sleep(1 + random.random())
        create_scr()
        time.sleep(random.random())
        coords = send_to_neuro()
        move_to_coords(coords)
        listen()
        click_rb()
        time.sleep(4 + random.random() + random.random())


start_fishing()
