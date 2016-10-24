#!/usr/bin/env python
import spell_number


def sort_lines(lines):
  return sorted(lines, key=lambda x: len(x[1]))


def generate_tuples(n):
  res = []
  for i in xrange(n):
    res.append((i + 1, spell_number.spell(i + 1)))
  return res


n = int(raw_input("Please enter N: "))
lines = generate_tuples(n)

print sort_lines(lines)
