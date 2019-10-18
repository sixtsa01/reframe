import pandas as pd
from refrom import Relation

def test_extend():
  data_real = {"name": ["Joe", "Jim", "Sam"], "salary": [60,40,20], "salary_new": [80,60,40]}
  data_expected = {"name": ["Joe", "Jim", "Sam"], "salary_diff": [20,20,20]
  df = pd.DataFrame(data=data_real)
  df_expected = pd.DataFrame(data=data_expected)
  r = Relation(df)
  r_expected = Relation(df_expected)
  r = r.extend("salary_diff", r.salary_new - r.salary)
  assert r.equals(r_expected)
  
