import serial #Импорт библиотеки serial
import time #Импорт библиотеки time
import serial.tools.list_ports #Импорт функции list_ports из модуля tools библиотеки serial
speeds = ['1200','2400', '4800', '9600', '19200', '38400', '57600', '115200'] #Создание списка speeds с различными скоростями передачи данных
ports = [p.device for p in serial.tools.list_ports.comports()] #Получение списка доступных портов и сохранение в переменную ports
port_name = ports[0] #Выбор первого порта из списка ports и сохранение в переменную port_name
port_speed = int(speeds[-1]) #Выбор максимальной скорости из списка speeds и преобразование в целое число, сохранение в переменную port_speed
port_timeout = 10 #Установка времени ожидания для порта
ard = serial.Serial(port_name, port_speed, timeout = port_timeout) #Открытие соединения с Arduino на выбранном порте с указанной скоростью и временем ожидания
time.sleep(1) #Пауза на 1 секунду
ard.flushInput() #Очистка буфера входных данных порта
try: #Чтение данных из Serial порта в бинарном формате
 msg_bin = ard.read(ard.inWaiting()) 
 msg_bin += ard.read(ard.inWaiting())
 msg_bin += ard.read(ard.inWaiting()) 
 msg_bin += ard.read(ard.inWaiting()) 
 msg_str_ = msg_bin.decode() #Попытка чтения данных из порта и декодирование в строку
 print(len(msg_bin)) #Вывод количества прочитанных байт
except Exception as e: #Обработка исключения в случае ошибки и вывод сообщения об ошибке
 print('Error!') 
ard.close() #Закрытие соединения с Arduino
time.sleep(1) #Пауза на 1 секунду
print(msg_str_) #Вывод полученного сообщения в виде строки.
