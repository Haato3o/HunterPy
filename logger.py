import time

def Log(string):
    t = time.gmtime()
    timestamp = f'{t.tm_hour-3}:{t.tm_min}:{t.tm_sec}'
    print(f'{timestamp} [DEBUG] {string}')