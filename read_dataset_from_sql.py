from sqlalchemy import create_engine
import random as rand
import pandas as pd
from pprint import pprint

engine = create_engine('sqlite:///file.db', echo=False)

names = ['Ringo', 'John', 'Paul', 'George']

# Generate some example data.
report = {}
for n in names:
    grades = []
    for i in range(5):
        grades.append(rand.choice(range(50,100)))
    report[n] = grades
pprint(report)

df = pd.DataFrame(report)
df.to_sql('grades', con=engine, if_exists='replace')

result = engine.execute('Select * from grades').fetchall()
pprint(result)
