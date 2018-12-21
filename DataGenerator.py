import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plot
import random


class Record:
    active = 1
    cpu = []
    mem = []
    cont_type_1 = []
    cont_type_2 = []
    cont_type_3 = []
    avg_resp_time = []

    def __init__(self):
        self.active = 1
        self.cpu = []
        self.mem = []
        self.cont_type_1 = []
        self.cont_type_2 = []
        self.cont_type_3 = []
        self.avg_resp_time = []
        pass


def generateNodeMetrics(active, date_rng, cpu_value, mem_value, cont_t1_value, cont_t2_value, cont_t3_value,
                        avg_resp_time, destroy_index):
    cpu_value = cpu_value
    mem_value = mem_value
    cont_t1_value = cont_t1_value
    cont_t2_value = cont_t2_value
    cont_t3_value = cont_t3_value
    avg_resp_time = avg_resp_time

    record = Record()

    i = 0
    y = 0
    z = 0

    while i < len(date_rng):
        if i == destroy_index:
            active = False
            cpu_value = 0
            mem_value = 0
            cont_t1_value = 0
            cont_t2_value = 0
            cont_t3_value = 0
            avg_resp_time = 0

        record.cpu.append(cpu_value)
        record.mem.append(mem_value)
        record.cont_type_1.append(cont_t1_value)
        record.cont_type_2.append(cont_t2_value)
        record.cont_type_3.append(cont_t3_value)
        record.avg_resp_time.append(avg_resp_time)

        i = i + 1

        if active:
            y = y + 1
            z = z + 1

            if y == 20:
                y = 0
                random_v = random.randint(0, 2)
                cpu_value_step = random.randint(5, 10)
                mem_value_step = random.randint(10, 15)
                avg_resp_time_value_step = random.randint(30, 60)
                if random_v == 0:
                    cpu_value = cpu_value + cpu_value_step
                    if cpu_value > 100:
                        cpu_value = 100
                    mem_value = mem_value + mem_value_step
                    if mem_value > 100:
                        mem_value = 100
                    avg_resp_time = avg_resp_time + avg_resp_time_value_step
                else:
                    cpu_value = cpu_value - cpu_value_step
                    if cpu_value < 5:
                        cpu_value = 5
                    mem_value = mem_value - mem_value_step
                    if mem_value < 10:
                        mem_value = 10
                    avg_resp_time = avg_resp_time - avg_resp_time_value_step
                    if avg_resp_time < 600:
                        avg_resp_time = 600

            if z == 5000:
                z = 0
                random_v = random.randint(0, 5)
                if random_v == 1:
                    cont_t1_value = cont_t1_value + 1
                    cpu_value = cpu_value + 10
                    if cpu_value > 100:
                        cpu_value = 100
                if random_v == 2:
                    cont_t1_value = cont_t1_value - 1

                random_v = random.randint(0, 5)
                if random_v == 1:
                    cont_t2_value = cont_t2_value + 1
                    mem_value = mem_value + 10
                    if mem_value > 100:
                        mem_value = 100
                if random_v == 2:
                    cont_t2_value = cont_t2_value - 1

                random_v = random.randint(0, 5)
                if random_v == 1:
                    cont_t3_value = cont_t3_value + 1
                if random_v == 2:
                    cont_t3_value = cont_t3_value - 1

    return record


date_rng = pd.date_range(start='10/10/2018', end='12/16/2018', freq='60s')

dataframe = pd.DataFrame(date_rng, columns=['timestamp'])
dataframe = dataframe.set_index('timestamp')

metrics_node1 = generateNodeMetrics(True, date_rng, 70, 50, 20, 15, 5, 1100, -1)
metrics_node2 = generateNodeMetrics(True, date_rng, 50, 40, 3, 0, 5, 1200, 50000)
metrics_node3 = generateNodeMetrics(True, date_rng, 80, 60, 15, 19, 12, 1500, -1)
metrics_node4 = generateNodeMetrics(False, date_rng, 0, 0, 0, 0, 0, 0, -1)

print len(metrics_node1.cpu)
print len(date_rng)

dataframe['node1_state'] = 1
dataframe['node1_cpu'] = metrics_node1.cpu
dataframe['node1_memory'] = metrics_node1.mem
dataframe['node1_cont_type_1'] = metrics_node1.cont_type_1
dataframe['node1_cont_type_2'] = metrics_node1.cont_type_2
dataframe['node1_cont_type_3'] = metrics_node1.cont_type_3
dataframe['node1_avg_resp_time'] = metrics_node1.avg_resp_time

dataframe['node2_state'] = 1
dataframe['node2_cpu'] = metrics_node2.cpu
dataframe['node2_memory'] = metrics_node2.mem
dataframe['node2_cont_type_1'] = metrics_node2.cont_type_1
dataframe['node2_cont_type_2'] = metrics_node2.cont_type_2
dataframe['node2_cont_type_3'] = metrics_node2.cont_type_3
dataframe['node2_avg_resp_time'] = metrics_node2.avg_resp_time

dataframe['node3_state'] = 1
dataframe['node3_cpu'] = metrics_node3.cpu
dataframe['node3_memory'] = metrics_node3.mem
dataframe['node3_cont_type_1'] = metrics_node3.cont_type_1
dataframe['node3_cont_type_2'] = metrics_node3.cont_type_2
dataframe['node3_cont_type_3'] = metrics_node3.cont_type_3
dataframe['node3_avg_resp_time'] = metrics_node3.avg_resp_time

dataframe['node4_state'] = 0
dataframe['node4_cpu'] = metrics_node4.cpu
dataframe['node4_memory'] = metrics_node4.mem
dataframe['node4_cont_type_1'] = metrics_node4.cont_type_1
dataframe['node4_cont_type_2'] = metrics_node4.cont_type_2
dataframe['node4_cont_type_3'] = metrics_node4.cont_type_3
dataframe['node4_avg_resp_time'] = metrics_node4.avg_resp_time

dataframe.to_csv('data/nodes_metrics.csv')

print dataframe.head(50)
