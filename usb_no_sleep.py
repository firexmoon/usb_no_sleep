
import threading
from datetime import datetime


# 要监控的目录
drivers = ['e:\\', 'm:\\']


# 定时器间隔（秒）
timer_dump_interval = 120
# 循环定时器
timer_dump = None


def update_file(driver):
    filename = driver + '.no_sleep'
    with open(filename, 'w') as fd:
        fd.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


# 循环定时器
def fun_timer_dump():
    global timer_dump
    print()
    
    for driver in drivers:
        try:
            update_file(driver)
            print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), ' update for ', driver)
        except:
            print('!!! ', datetime.now().strftime('%Y-%m-%d %H:%M:%S'), ' except for ', driver)
    
    print()
    timer_dump = threading.Timer(timer_dump_interval, fun_timer_dump)
    timer_dump.start()
        
        
if __name__ == '__main__':
    fun_timer_dump()
    