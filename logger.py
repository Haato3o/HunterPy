import time

def Log(string):
    t = time.gmtime()
    timestamp = f'{t.tm_hour}:{t.tm_min}:{t.tm_sec}'
    print(f'{timestamp} [DEBUG] {string}')