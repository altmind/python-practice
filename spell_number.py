from __future__ import division

NUMBERS_MAP = {
  1: "one",
  2: "two",
  3: "three",
  4: "four",
  5: "five",
  6: "six",
  7: "seven",
  8: "eight",
  9: "nine",
  10: "ten",
  11: "eleven",
  12: "twelve",
  13: "thirteen",
  14: "fourteen",
  15: "fifteen",
  16: "sixteen",
  17: "seventeen",
  18: "eighteen",
  19: "nineteen",
  20: "twenty",
  30: "thirty",
  40: "forty",
  50: "fifty",
  60: "sixty",
  70: "seventy",
  80: "eighty",
  90: "ninety",
}
NUMBERS_SCALE = {
  0: '',
  # 2: 'hundred',
  3: 'thousand',
  6: 'million',
  9: 'billion',
  12: 'trillion',
  15: 'quadrillion',
  18: 'quintillion',
  21: 'sextillion',
  24: 'septillion',
  27: 'octillion',
  30: 'nonillion',
  33: 'decillion'
}


def _spell_under_thousand(number):
  remainder = number
  result = ""
  if (remainder > 99):
    hundreds = int(remainder // 100)
    result = NUMBERS_MAP[hundreds] + " hundred "
    if (hundreds > 1):
      result + "s"
    remainder = remainder % 100
  if (remainder == 0):
    pass
  elif (remainder > 0 and remainder <= 20):
    result = result + NUMBERS_MAP[remainder]
  else:
    result = result + NUMBERS_MAP[10 * int(remainder // 10)]
    remainder = remainder % 10
    if remainder > 0:
      result = result + "-" + NUMBERS_MAP[remainder % 10]
  return result


def spell(number):
  remainder = number
  result = ""
  scales = list(reversed(NUMBERS_SCALE.keys()))

  if (remainder < 0):
    remainder = -remainder
    result = "minus "
  elif (remainder == 0):
    return "zero"

  while len(scales) > 0:
    this_power = scales.pop(0)
    this_scale = (10 ** this_power)
    this_slice = int(remainder // this_scale)
    if this_slice > 0:
      optional_plural = ""
      # if (this_slice % 10 > 1):
      #   optional_plural = "s"
      power_in_words = ""
      if (len(NUMBERS_SCALE[this_power]) > 0):
        power_in_words = " " + NUMBERS_SCALE[this_power] + optional_plural
      result = result + _spell_under_thousand(this_slice) + power_in_words + " "
    remainder = remainder % this_scale
  return result.strip()
