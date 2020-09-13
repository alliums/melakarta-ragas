# -*- coding: utf-8 -*-

from ratioDict import ratios
import fileinput
import string

print("Shruti to Interval Ratio Translator ")


inFilename = raw_input("enter full the filename of your input file: ")
outFilename = raw_input("enter full the filename of your output file: ")

inFile = open(inFilename, "r")
inLines = inFile.readlines()
raw = []


for scale in inLines:
    splitScale = scale.split(" ")
    print(splitScale)
    raw.append(splitScale)

    #print(i.split("\n"))

print(raw)


print("~~~~~")

scales = []
for i in raw:
    currentScale  = []
    for j in i:
        currentScale.append(ratios.get(j.strip("\n")))
    print(currentScale)
    scales.append(currentScale)


outFile = open(outFilename, "w")
for i in scales:
    for j in i:
        outFile.write(j + " ")
    outFile.write("\n")




# S 1
# R1  32/31
# R2  "16/15"
# R3  10/9
# G1  32/27
# G2  6/5
# G3  5/4
# M1  4/3
# M2 27/20
# P 3/2
# D1 128/81
# D2 8/5
# D3 5/3
# N1 16/9
# N2 9/5
# N3 15/8



# Swara Ratio Swara Ratio
# S 1
# R1  32/31
# R2  16/15
# R3  10/9
# G1  32/27
# G2  6/5
# G3  5/4
# M1  4/3
# M2 27/20
# P 3/2
# D1 128/81
# D2 8/5
# D3 5/3
# N1 16/9
# N2 9/5
# N3 15/8
##IJCSI International Journal of Computer Science Issues, Vol. 7, Issue 4, No 7, July 2010
##ISSN (Online): 1694-0784
##ISSN (Print): 1694-0814
##Fundamental Frequency Estimation of Carnatic Music
##Department of Computer Science and Engineering
##Anna University, Chennai, India
