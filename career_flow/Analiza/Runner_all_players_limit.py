import os
from multiprocessing.pool import ThreadPool

def worker_func(a):
	s1="py All_players_points_and_positions_limit.py "+str(a)+" "+str(a+100)
	os.system(s1)
	print(s1)
	#print(a,a+100)

pool = ThreadPool(processes=4)
nums = list(range(0,11000,4000))
pool.map(worker_func, nums)

pool.close()
pool.join()