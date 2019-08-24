from sqlalchemy import create_engine
import random as rand
import pandas as pd

engine = create_engine('sitelite:///', echo=False)

names = ['Ringo', 'John', 'Paul', 'George']
report = {}

for n in names:
    grades = []
    for i in range(5):
        grades.append(rand.choice(range(50,100)))
    report[n] = grades

report
