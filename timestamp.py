import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plot
import random

date_rng = pd.date_range(start='10/10/2018', end='12/16/2018', freq='60s')

# df = pd.DataFrame(date_rng, columns=['node1_status', 'node1_cpu', 'node1_memory','node1_amount_cont_1', 'node1_amount_cont_2'])


class Record:
    cpu=[]
    mem=[]


df = pd.DataFrame(date_rng, columns=['timestamp'])
df = df.set_index('timestamp')
df['node1_status'] = 1

cpu = []
mem = []
cont_type_1 = []

cpu_value = 70
mem_value = 50
node1_amount_cont_1 = 10
node1_amount_cont_2 = 20
node1_amount_cont_3 = 15

i = 0
y = 0
z = 0
while i < len(date_rng):
    cpu.append(cpu_value)
    mem.append(mem_value)
    cont_type_1.append(node1_amount_cont_1)
    i = i + 1
    y = y + 1
    z = z + 1
    if y == 20:
        y = 0
        random_v = random.randint(0, 1)
        cpu_value_step = random.randint(5, 10)
        mem_value_step = random.randint(10, 15)
        if random_v == 0:
            cpu_value = cpu_value + cpu_value_step
            if cpu_value > 100:
                cpu_value = 100
            mem_value = mem_value + mem_value_step
            if mem_value > 100:
                mem_value = 100
        else:
            cpu_value = cpu_value - cpu_value_step
            if cpu_value < 20:
                cpu_value = 20
            mem_value = mem_value - mem_value_step
            if mem_value < 10:
                mem_value = 10
    if z == 5000:
        z = 0
        random_v = random.randint(0, 4)
        if random_v == 1:
            node1_amount_cont_1 = node1_amount_cont_1 + 1
        if random_v == 2:
            node1_amount_cont_1 = node1_amount_cont_1 - 1

def generateNodeMetrics(date_rng):
    cpu_value = 70
    mem_value = 50

    record = Record()

    i = 0
    y = 0
    z = 0
    while i < len(date_rng):
        record.cpu.append(cpu_value)
        record.mem.append(mem_value)

        i = i + 1
        y = y + 1

        if y == 20:
            y = 0
            random_v = random.randint(0, 1)
            cpu_value_step = random.randint(5, 10)
            mem_value_step = random.randint(10, 15)
            if random_v == 0:
                cpu_value = cpu_value + cpu_value_step
                if cpu_value > 100:
                    cpu_value = 100
                mem_value = mem_value + mem_value_step
                if mem_value > 100:
                    mem_value = 100
            else:
                cpu_value = cpu_value - cpu_value_step
                if cpu_value < 20:
                    cpu_value = 20
                mem_value = mem_value - mem_value_step
                if mem_value < 10:
                    mem_value = 10

    return record


node1 = generateNodeMetrics(date_rng)

print node

df['node1_cpu'] = cpu
df['node1_memory'] = mem  # np.random.randint(60, 100, size=(len(date_rng)))
df['node1_amount_cont_1'] = cont_type_1
df['node1_amount_cont_2'] = 20
df['node1_amount_cont_3'] = 20

df.to_csv('data/nodes.csv')

visual_df = pd.read_csv('data/nodes.csv', index_col='timestamp', parse_dates=True)

# visual_df = visual_df.set_index('timestamp')
#
#
# visual_df = visual_df.sort_index()

visual_df = visual_df.loc['10/10/2018':'12/12/2018', ['node1_amount_cont_1']]
# # visual_df=  df['node1_cpu']
visual_df.plot()
plot.show()
