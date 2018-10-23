# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re


import csv
import sys
csv.field_size_limit(sys.maxsize)


def doesStrMatchRegex(regex, s):
  return numMatches(regex, s) > 0

def numMatches(regex, s):
  matches = re.finditer(regex, s, re.MULTILINE)

  total = 0
  list_matches = list(matches)
  for matchNum, match in enumerate(list_matches):
    matchNum = matchNum + 1

    # print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(), end=match.end(), match=match.group()))

    for groupNum in range(0, len(match.groups())):
      groupNum = groupNum + 1

      print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum, start=match.start(groupNum), end=match.end(groupNum), group=match.group(groupNum)))
  return (len(list_matches))

dontMatchRegexes = [
  # r"MORE_HOMES_IN_HIGHER_PRICE_MAX",
  # r"MORE_HOMES_IN_ZOOMED_OUT_MAP",
  # r"sectionType.{1,10}HOMES_LOW_INVENTORY_PRICE_MAX",
  # r"guided_search_low_inventory_price_max_v3.{1,10}treatment.{1,10}treatment",
]

regexes = [
  # r"sectionType.{1,10}HOMES_LOW_INVENTORY_PRICE_MAX",
  # r"MORE_HOMES_IN_HIGHER_PRICE_MAX",
  # r"guided_search_low_inventory_price_max_v3.{1,10}treatment.{1,10}treatment",
  # r"guided_search_p2_wishlist_grouping_v2.{1,10}treatment.{1,10}treatment",
  r"guided_search_p2_wishlist_grouping_v2.{1,10}treatment.{1,10}control",
  # r"guided_search_low_inventory_price_max_v3.{1,10}treatment.{1,10}control",
  # r"MORE_HOMES_IN_ZOOMED_OUT_MAP",
  r"EXPERIMENT_DUMMY",
]

with open('file_name_clay.tsv', 'rb') as csvfile:
# with open('logs_price_v3.tsv', 'rb') as csvfile:
  numMatchingRows = 0
  numTotalRows = 0
  for row in csv.reader(csvfile, delimiter='\t'):
    numTotalRows += 1
    rowStr = ', '.join(row)
    matchesAll = True
    for regex in dontMatchRegexes:
      if doesStrMatchRegex(regex, rowStr):
        matchesAll = False
        break
    if not matchesAll:
      continue
    for regex in regexes:
      if not doesStrMatchRegex(regex, rowStr):
        matchesAll = False
        break
    if matchesAll:
      numMatchingRows += 1
      # print(rowStr)
      # break

  print regexes
  print 'numMatchingRows:', numMatchingRows
  print 'numTotalRows:', numTotalRows
  print 'percent matching:', float(numMatchingRows) / numTotalRows
