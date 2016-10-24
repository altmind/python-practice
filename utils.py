import sys


def die(message):
  print message
  sys.exit(1)


def avg(l):
  return sum(l) / float(len(l))
