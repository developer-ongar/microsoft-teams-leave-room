import time
import keyboard

print("\nCurrent time is",time.strftime("%H:%M:%S", time.localtime()))

def take_time_input():
    time_to_leave=input(str("\nВведите время, чтобы покинуть класс. Например:- 14:05:00  --->   "))
    
    if time_to_leave > time.strftime("%H:%M:%S", time.localtime()):
    
        return time_to_leave

    else:
        print("\nВремя ввода превышает текущее время или имеет неверный формат")
        take_time_input()
    

time_to_leave=take_time_input()

while True :

    if  time.strftime("%H:%M:%S", time.localtime()) > time_to_leave:
        keyboard.press_and_release('ctrl', 'shift','B')
        print("\nНажал ctrl, shift, B. Совещание завершилось.\n")
        break

    time.sleep(10)
