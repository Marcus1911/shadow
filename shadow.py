# Designed with XGH
# by Marcus Sandri
# v 1.0

import os, subprocess

# Globals
cmd = "ps -A | grep gedit"  #TODO: input external parameter





def kill_process(process):
	#XXX: Used to kill process
	os.system("kill -9 " + process)



def handle_process(command): 
	#XXX: captura processo + saida
	try:
		ps = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
		output = ps.communicate()[0]
		str_pid = output.split()
		pid_to_kill = str_pid[0]
		print pid_to_kill

		kill_process(pid_to_kill)

	except IndexError:
		if (IndexError):
			handle_process(cmd)
			print "hehe"


# call
handle_process(cmd)
