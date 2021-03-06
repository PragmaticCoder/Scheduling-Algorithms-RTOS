#!/usr/bin/python

from Utility import *

def schedule_lst(task_info):
	print("LST Scheduler")
	task_info.sort(key=lambda x: x[5]) # sort on slack time
	print_task_info(task_info)

	time = 0.0
	current_process = 0
	total_tasks = len(task_info)
	last_process = 0

	while(time <= SIMULATION_TIME):
		print("At Time : " + str(time))
		current_process = -1

		for i in range(0, total_tasks):
			if(task_info[i][3] <= time):
				current_process = i;
				break;

		
		if ((current_process != last_process) and task_info[last_process][6] > 0.0):
			print("\tPRE-EMPTING TASK " + str(task_info[last_process][0]))
			task_info[last_process][7] = task_info[last_process][7] + 1
		print("\tEXECUTING TASK " + str(task_info[current_process][0]))

		if (current_process > -1):
			task_info[current_process][6] = task_info[current_process][6] + 1.0
			
			if (task_info[current_process][6] == task_info[current_process][2]):
				
				print("\tTASK COMPLETED " + str(task_info[current_process][0]))
				task_info[current_process][9] += 1
				task_info[current_process][10] += (float(time) + 1.0 - task_info[current_process][3])
				task_info[current_process][3] += task_info[current_process][1]
				task_info[current_process][4] = task_info[current_process][3] + task_info[current_process][1]
				task_info[current_process][6] = 0.0
		
		for i in range(0, total_tasks):
			if(task_info[i][4] < time):
				print("\tTASK " + str(task_info[i][0]) + " MISSED DEADLINE!!");
				task_info[i][8] = task_info[i][8] + 1
				task_info[i][3] += task_info[i][1]
				task_info[i][4] = task_info[i][3] + task_info[i][1]
				task_info[i][6] = 0.0

		time += 1.0
		last_process = current_process
		task_info.sort(key=lambda x: x[5]) # sort on slack time

	print_task_info(task_info)
