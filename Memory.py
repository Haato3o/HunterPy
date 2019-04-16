from ctypes import *
from ctypes.wintypes import *
import struct

class Memory:
    ALL_ACCESS = 0x1F0FFF
    INT = 4
    CHAR = 1
    FLOAT = 4
    LONG = 4

    def __init__(self, pid):
        self.pid = pid
        self.ReadMemory = WinDLL('kernel32').ReadProcessMemory
        self.OpenProcess = windll.kernel32.OpenProcess
        self.pHandle = None
        self.getProcessHandle()

    def getProcessHandle(self):
        processHandle = self.OpenProcess(Memory.ALL_ACCESS, 0, self.pid)
        self.pHandle = processHandle

    def readString(self, address, size):
        buffer = create_string_buffer(size)
        bRead = c_size_t()
        self.ReadMemory(self.pHandle, c_void_p(address), buffer, size, byref(bRead))
        return bytearray(buffer[0: size])

    def readInteger(self, address):
        buffer = create_string_buffer(Memory.INT)
        bRead = c_size_t()
        self.ReadMemory(self.pHandle, c_void_p(address), buffer, Memory.INT, byref(bRead))
        result = struct.unpack("I", buffer[0: Memory.INT])[0]
        return result

    def readFloat(self, address):
        buffer = create_string_buffer(Memory.FLOAT)
        fRead = c_size_t()
        self.ReadMemory(self.pHandle, c_void_p(address), buffer, Memory.FLOAT, byref(fRead))
        result = struct.unpack('f', buffer[0: Memory.FLOAT])[0]
        return result