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
  assert len(df_region) == len(df_union)

def test_union2():
  df = Relation("../country.csv")
  df_region = df.query("region == 'North America'")
  df_union = df_region.union(df_region)
  assert len(df_region) == len(df_union)
