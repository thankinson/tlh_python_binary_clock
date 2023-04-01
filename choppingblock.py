import time
import board
from adafruit_ht16k33.matrix import Matrix8x8

i2c = board.I2C()
matrix = Matrix8x8(i2c)

t = time.localtime()
curent_time = time.strftime("%H:%M:%S", t)
hour = time.strftime("%H", t)
min = time.strftime("%M", t)
sec = time.strftime("%S", t)
print(curent_time)
print("Hour: ", hour)
print("Min: ", min)
print("Sec: ", sec)

# This function converts the time to binary
def TimeToBinary(number):
        num = int(number)
        b = ""

        if (num == 0):
                return 0
        while ( num ):
                b +=  str(num&1)
                num = num >> 1

        b = b[::-1]
        return int(b)

# This function takes the hour/min/second binary and converts it to an array
def BinaryList(number):
        binary = [int(i) for i in str(number)]

        for i in range(len(binary) // 2):
                binary[i], binary[-1 - i] = binary[-1 - i], binary[i]

        return binary

# this function displays the binary on the adafruit led 8x8 matrix display
def DisplayTime(num, time):
        t = len(time)

        for i in range(t):
                matrix[num, i] = time[i]

print("hour: ",hour, "binary: ", BinaryList(TimeToBinary(hour)))
print("min: ",min, "binary: ", BinaryList(TimeToBinary(min)))
print("second: ",sec, "binary: ", BinaryList(TimeToBinary(sec)))

curr_hour = BinaryList(TimeToBinary(hour))
curr_min = BinaryList(TimeToBinary(min))
curr_sec = BinaryList(TimeToBinary(sec))

DisplayTime(7, curr_hour)
DisplayTime(5, curr_min)
DisplayTime(3, curr_sec)
# 