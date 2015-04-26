#!/usr/bin/env python3
import codecs,sys
input = sys.stdin.read()
output = codecs.encode(input,"rot13")
print( output ,end="")
