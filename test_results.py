# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 13:25:38 2022

@author: Lijin N S
"""

import os
import glob
import time
import filecmp

weblink = #test label submission weblink
datalink = #updated test data weblink

completed_runs = len(os.listdir('test_data'))
run = 0
for iter in range(500):
    print('Iteration {}'.format(iter+1))
    print('Phase {}'.format(completed_runs+run+1))
    for each_file in os.listdir('results'):
        del_file = 'results/'+each_file
        os.remove(del_file)
    
    
    
    os.system('python3 testing_selfharm_prediction.py --model 1 &')
    os.system('python3 testing_selfharm_prediction.py --model 2 &')
    os.system('python3 testing_selfharm_prediction.py --model 3 &')
    os.system('python3 testing_selfharm_prediction.py --model 4 &')
    os.system('python3 testing_selfharm_prediction.py --model 5 &')    
        
    task_list = [0,0,0,0,0]

    while(True):
        if sum(task_list) == 5:
            break
        if len(glob.glob('results/*svm_e*')) == 1 and task_list[0] == 0:
            os.system('curl  -H "Content-Type:application/json" -w "%{http_code}" -X POST -d @./{}/0 '.format(weblink))
            task_list[0] = 1
        if len(glob.glob('results/*svm_t*')) == 1 and task_list[1] == 0:
            os.system('curl  -H "Content-Type:application/json" -w "%{http_code}" -X POST -d @./{}/1 '.format(weblink))    
            task_list[1] = 1
        if len(glob.glob('results/*rf_e*')) == 1 and task_list[2] == 0:
            os.system('curl  -H "Content-Type:application/json" -w "%{http_code}" -X POST -d @./{}/2 '.format(weblink))            
            task_list[2] = 1
        if len(glob.glob('results/*rf_d*')) == 1 and task_list[3] == 0:
            os.system('curl  -H "Content-Type:application/json" -w "%{http_code}" -X POST -d @./{}/3 '.format(weblink))            
            task_list[3] = 1
        if len(glob.glob('results/*ab_e*')) == 1 and task_list[4] == 0:
            os.system('curl  -H "Content-Type:application/json" -w "%{http_code}" -X POST -d @./{}/4 '.format(weblink))
            task_list[4] = 1
        else:
            time.sleep(0.5)
    
    os.system('wait')
    os.chdir('test_data')
    print('Getting Training Data - Next Phase')
    os.system('wget ' + datalink)
    time.sleep(3)

    os.rename('UdnOqz18pprZy5wbRCNEC7YcA81n7IT51L0IQL7Vqp8','t2_test_data{}.json'.format(completed_runs+run+1))
    
    if filecmp.cmp('t2_test_data{}.json'.format(completed_runs+run),'t2_test_data{}.json'.format(completed_runs+run+1)):
        print('Same test data in successive iterations.')
        os.remove('t2_test_data{}.json'.format(completed_runs+run+1))
    else: 
        run += 1
        
    os.chdir('..')
    
    print('Phase {} completed !!\n'.format(completed_runs+run))
    
