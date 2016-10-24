#!/usr/bin/env python
# import csv # use csv or dummy csv impl
import dummy_csv as csv
from utils import *


def csv_to_tuples(input_fh):
  result = {}
  with input_fh:
    csv_reader = csv.reader(input_fh)
    headers = next(csv_reader, None)  # Skip headers
    for row in csv_reader:
      symbol, bid, bid_qty, ask, ask_qty = row
      if symbol not in result:
        result[symbol] = {"bid": [], "ask": []}
      result[symbol]["bid"].append((float(bid), float(bid_qty)))
      result[symbol]["ask"].append((float(ask), float(ask_qty)))
    # Generate avgs over collected data
    for symbol in result:
      bids = [x[0] for x in result[symbol]["bid"]]
      asks = [x[0] for x in result[symbol]["ask"]]
      result[symbol]["avg_bid_qty"] = round(avg(bids), 2)
      result[symbol]["avg_ask_qty"] = round(avg(asks), 2)
  return result


if len(sys.argv) != 2:
  die("Program requires exactly 1 argument")

input_file_name = sys.argv[1]

try:
  input_fh = open(input_file_name, "rb")
  print csv_to_tuples(input_fh)
except IOError:
  die("Could not read file: %s" % input_file_name)
