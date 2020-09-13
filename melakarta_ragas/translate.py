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
    
