# https://habr.com/post/187482/
import psutil
from time import time

'''
def timed(fn):
    def decorated(*x):
        start = time()
        result = fn(*x)
        print ("Executing %s took %d ms" % (fn.__name__, (time() - start)*1000))
        return result
    return decorated'''

def repeat(times):
    """ повторить вызов times раз, и вернуть среднее значение """
    def decorator(fn):
        def decorated2(*x):
            total = 0
            for i in range(times):
                total += fn(*x)
            return total / times
        return decorated2
    return decorator

@repeat(5)
def cpuload():
    load = psutil.cpu_percent()
    print ("cpuload() returns %d" % load)
    return load

print ("cpuload.__name__==" + cpuload.__name__)
print ("CPU load is %d%%" % cpuload())
print(psutil.cpu_stats())
print(psutil.sensors_battery())
#print(psutil.temperature(fahrenheit=False))
#print(psutil.sensors_fans())
