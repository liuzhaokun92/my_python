# # # # import subprocess
# # # # print('$ nslookup www.python.org')
# # # # r=subprocess.call(['nslookup','www.python.org'])
# # # # print('Exit code:',r)

# # # from multiprocessing import Pool

# # # import os,time,random
# # # def long_time_task(name):
# # # 	print('Run task %s (%s)...'%(name,os.getpid()))
# # # 	start=time.time()
# # # 	time.sleep(random.random()*3)
# # # 	end=time.time()
# # # 	print('Task %s run %0.2f seconds.'%(name,(end-start)))
# # # if __name__=='__main__':
# # # 	print('Parent process %s .'%os.getpid())
# # # 	p=Pool(4)
# # # 	for i in range(5):
# # # 		p.apply_async(long_time_task,args=(i,))
# # # 	print('Waiting for all subprocess done...')
# # # 	p.close()
# # # 	p.join()
# # # 	print('All subprocesses done.')


# # import os 
# # #only works on Unix/Linux/Mac
# # print('Progress (%s) start...' %os.getppid())
# # if pid==0:
# # 	print('I am child Progress (%s) and parent is %s.'%(os.getpid(),os.getppid))
# # else:
# # 	print('I (%s) just created a child progress(%s).'%(os.getpid(),pid))
# # 	
# from multiprocessing import Process
# import os
# def run_proc(name):
# 	print('Run child process %s (%s)...'%(name,os.getpid()))
# if __name__=='__main__':
# 	print('Parent process %s.' %os.getpid())
# 	p=Process(target=run_proc,args=('test',))
# 	print('Child process will start')
# 	p.start()
# 	p.join()
# 	print('Child process end.')
