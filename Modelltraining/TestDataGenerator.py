import numpy as np
import random

file = open("test1k.csv", "w")
file.write("Time,Feature1,Feature2\n")

for i in range(1000):
    file.write(f"{i*1000+1732266000000},{random.randrange(0, 1000)/1000},{random.randrange(0, 1000)/1000}\n")
    if i % 1000:
        print(f"{i/10000}%")
print("Finished!")
