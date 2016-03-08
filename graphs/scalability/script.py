#!/usr/bin/env python

f = open("scaling.dat", "r")
fw = open("new_scaling.dat", "w")

for line in f.readlines():
  line = line.split()
  line[1] = str(float(line[1]) / 1000)
  line[2] = str(float(line[2]) / 1000)
  line[3] = str(float(line[3]) / 1000)
  fw.write(" ".join(line)+"\n")
