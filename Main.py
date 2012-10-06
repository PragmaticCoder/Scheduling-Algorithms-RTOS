#!/usr/bin/python

import sys

from Utility import *
from RMS_Scheduler import *
from EDF_Scheduler import *
from LST_Scheduler import *

def check_input_format_and_load(input_lines):
	
	task_info = []
	for each in input_lines:
		temp = each.strip().split(",")
		if (len(temp) != 3):
			return -1
		else:
			try:
				task_id = int(temp[0].strip())
				period = float(temp[1].strip())
				wcet = float(temp[2].strip())
				a_time = 0.0
				deadline = a_time + period
				ceu = 0.0
				slack_time = (deadline - 0.0) - (wcet - ceu)
				pre_emption_count = 0
				deadline_misses = 0 
				completion_count = 0
				cumulative_response_time = 0.0
				temp_list = [task_id, period, wcet, a_time, deadline, slack_time, ceu, pre_emption_count, deadline_misses, completion_count, cumulative_response_time]
				task_info.append(temp_list)
			except ValueError:
				return -1
	return task_info


def main():

	if (len(sys.argv) != 3):
		print("Usage: python Main.py <path to input file> <rms|lst|edf>")

	else:
		try:
			input_file = open(sys.argv[1], "r")
			input_lines = input_file.readlines()
			task_info = check_input_format_and_load(input_lines)

			if task_info == -1:
				print("Input file not in correct format")
			else:
				if (str(sys.argv[2]) == "rms"):
					print_task_info(task_info)
					schedule_rms(task_info)
				elif (str(sys.argv[2]) == "edf"):
					print_task_info(task_info)
					schedule_edf(task_info)
				elif (str(sys.argv[2]) == "lst"):
					print_task_info(task_info)
					schedule_lst(task_info)
				else:
					print("Usage: python Main.py <path to input file> <rms|lst|edf>")

			input_file.close()
		except IOError:
			print("ERROR!! : File does not exist (or) I/O Error")
			print("Usage: python Main.py <path to input file> <rms|lst|edf>")


main()
