#!/usr/bin/python

SIMULATION_TIME = 20

def print_task_info(task_info):
	print("Task\tPeriod\tWCET\tArrivalTime\tDeadline\tSlackTime\t#Pre-empts\t#deadline misses\t#completions\tcum_resp_time\tavg_resp_time")
	for each in task_info:
		if each[10] == 0.0:
			temp = 0.0 
		else:
			temp = (float(each[10])/float(each[9]))
		print(str(each[0]) + "\t" + str(each[1]) + "\t" + str(each[2]) + "\t" + str(each[3]) + "\t\t" + str(each[4]) + "\t\t" + str(each[5]) + "\t\t\t" + str(each[7])+ "\t\t" + str(each[8]) + "\t\t" + str(each[9]) + "\t\t" + str(each[10])+ "\t\t"+ str(temp))



