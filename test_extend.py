""" My VMWare Station was not able to download pytest. I tried reinstalling Python to see if it would help, but it did not help
I was not able to test the tests completely, but I went off of what we did in class to make my tests"""

import pandas as pd
from reframe import Relation

def test_extend1():
  data_real = {"name": ["Joe", "Jim", "Sam"], "salary": [60,40,20], "salary_new": [80,60,40]}
  data_expected = {"name": ["Joe", "Jim", "Sam"], "salary": [60,40,20], "salary_new": [80,60,40], "salary_diff": [20,20,20]}
  df = pd.DataFrame(data=data_real)
  df_expected = pd.DataFrame(data=data_expected)
  r = Relation(df)
  r_expected = Relation(df_expected)
  r = r.extend("salary_diff", r.salary_new - r.salary)
  assert r.equals(r_expected)

                   
def test_extend2():
  data_real = {"name": ["Sandy", "Deb", "Alex"], "age": [18,21,44], "age_real": [22,23,50]}
  data_expected = {"name": ["Sandy", "Deb", "Alex"], "age": [18,21,44], "age_real": [22,23,50], "age_diff": [4,2,6]}
  df = pd.DataFrame(data=data_real)
  df_expected = pd.DataFrame(data=data_expected)
  r = Relation(df)
  r_expected = Relation(df_expected)
  r = r.extend("age_diff", r.age_real - r.age)
  assert r.equals(r_expected)

def test_extend3():
  data_real = {"name": ["Karissa", "Syd", "Brooke"], "gpa": [3,3,2], "gpa_real": [4,4,3]}
  data_expected = {"name": ["Karissa", "Syd", "Brooke"], "gpa": [3,3,2], "gpa_real": [4,4,3], "gpa_diff": [1,1,1]}
  df = pd.DataFrame(data=data_real)
  df_expected = pd.DataFrame(data=data_expected)
  r = Relation(df)
  r_expected = Relation(df_expected)
  r = r.extend("gpa_diff", r.gpa_real - r.gpa)
  assert r.equals(r_expected)
