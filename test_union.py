import sys
sys.path.insert(1, '../')
import pytest
import sys
import pandas as pd
from reframe import Relation

def test_union1():
  df = Relation("../country.csv")
  df_region = df.query("region == 'North America'")
  df_union = df_region.union(df_region)
  assert (len(df_region)*2) == len(df_union)

def test_union2():
  df = Relation("../country.csv")
  df_indepyear = df.query("indepyear == 1901")
  df_union = df_indepyear.union(df_indepyear)
  assert (len(df_indepyear)*2) == len(df_union)
  
def test_union3():
  df = Relation("../country.csv")
  df_continent = df.query("continent == 'Asia'")
  df_union = df_continent.union(df_continent)
  assert (len(df_continent)*2) == len(df_union)
