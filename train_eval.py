# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 13:29:15 2022

@author: Lijin N S
"""

from selfharm_prediction import selfharm_prediction
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--model', metavar='M', type=int, default=2,
                    help=' select which task to train/eval')
args = parser.parse_args()

if args.model == 1:
    print('SVM_E_500 model')
    clf = selfharm_prediction('/home/interns/erisk2022/depressiondata/',model='entropy',model_path='saved_models/',clf_opt='svm',no_of_selected_features=500,output_file = 'results/svm_entropy_500.json')
if args.model == 2:
    print('SVM_T_200 model')
    clf = selfharm_prediction('/home/interns/erisk2022/depressiondata/',model='tfidf',model_path='saved_models/',clf_opt='svm',no_of_selected_features=200,output_file = 'results/svm_tfidf_200.json')
if args.model == 3:
    print('RF_E_2000 model')
    clf = selfharm_prediction('/home/interns/erisk2022/depressiondata/',model='entropy',model_path='saved_models/',clf_opt='rf',no_of_selected_features=2000,output_file = 'results/rf_entropy_2000.json')
if args.model == 4:
    print('RF_D_70 model')
    clf = selfharm_prediction('/home/interns/erisk2022/depressiondata/',model='doc2vec',model_path='saved_models/',clf_opt='rf',no_of_selected_features=70,output_file = 'results/rf_doc2vec_70.json')
if args.model == 5:
    print('AB_E_200 model')
    clf = selfharm_prediction('/home/interns/erisk2022/depressiondata/',model='entropy',model_path='saved_models/',clf_opt='ab',no_of_selected_features=200,output_file = 'results/ab_entropy_200.json')


clf.selfharm_prediction()
