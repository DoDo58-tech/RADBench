# 测试自己生成的Feature

#Import scikit-learn dataset library
from sklearn import datasets
from sklearn.model_selection import GridSearchCV
import numpy as np
from sklearn.metrics import confusion_matrix
#Load dataset

import pandas as pd
# load dataset
# names=['cliquedistance0', 'cliquedistance1', 'cliquedistance2','address0','address1','address2','degree0','degree1','degree2','transitdegree0','transitdegree1','transitdegree2','type0','type1','type2','rir','country','ixp',\
#        'asaverage_neighbor_degree0','asaverage_neighbor_degree1','asaverage_neighbor_degree2','asbetweenesscentrality0','asbetweenesscentrality1','asbetweenesscentrality2','ascloseness_centrality0','ascloseness_centrality1','ascloseness_centrality2',\
#                'asclusteringcoefficient0','asclusteringcoefficient1','asclusteringcoefficient2','aseigenvector_centrality0','aseigenvector_centrality1','aseigenvector_centrality2',\
#                 'asmaxcliquesize0','asmaxcliquesize1','asmaxcliquesize2','asrouternumber0','asrouternumber1','asrouternumber2','assquare_clustering0','assquare_clustering1','assquare_clustering2','astriangles_clustering0','astriangles_clustering1','astriangles_clustering2','label']


# pima = pd.read_csv("allsample.csv", header=None, usecols=[4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53],names=names)

# 去除了未知计算过程的Feature
# names=['cliquedistance0', 'cliquedistance1', 'cliquedistance2','address0','address1','address2','degree0','degree1','degree2','type0','type1','type2','rir','country','ixp',\
#        'asbetweenesscentrality0','asbetweenesscentrality1','asbetweenesscentrality2','ascloseness_centrality0','ascloseness_centrality1','ascloseness_centrality2',\
#                'asclusteringcoefficient0','asclusteringcoefficient1','asclusteringcoefficient2','aseigenvector_centrality0','aseigenvector_centrality1','aseigenvector_centrality2',\
#                 'asrouternumber0','asrouternumber1','asrouternumber2','assquare_clustering0','assquare_clustering1','assquare_clustering2','label']
# pima = pd.read_csv("allsample.csv", header=None, usecols=[4,5,6,7,8,9,10,11,12,16,17,19,20,21,22,26,27,28,29,30,31,32,33,34,38,39,40,44,45,46,47,48,49,53],names=names)

# 去除了暂时不能计算的Feature
# names=[
#         'asDistance0', 'asDistance1', 'asDistance2',\
#         'asDegree0','asDegree1','asDegree2',\
#         'asAddressSpace0','asAddressSpace1','asAddressSpace2',\
#         'asCountry0','asCountry1','asCountry2',\
#         # 'asRIR0','asRIR1','asRIR2',\
#         'asType0','asType1','asType2',\
#         'asCentrality0','asCentrality1','asCentrality2',\
#         'asClusteringCoefficient0','asClusteringCoefficient1','asClusteringCoefficient2',\
#         'asRouterNumber0','asRouterNumber1','asRouterNumber2',\
#         # 'ixp',\
#         'label'
#     ]
# pima = pd.read_csv("reGenerateSamples.csv", header=None, usecols=[
#     4,5,6,\
#     7,8,9,\
#     10,11,12,\
#     13,14,15,\
#     # 16,17,18,\
#     19,20,21,\
#     22,23,24,\
#     25,26,27,\
#     28,29,30,\
#     31
#     ],names=names)
featureNames=[
    'asDistance0', 'asDistance1', 'asDistance2',
    'asDegree0','asDegree1','asDegree2',
    'asAddressSpace0','asAddressSpace1','asAddressSpace2',
    'asCountry','asRIR',
    'asType0','asType1','asType2',
    'asBetweennessCentrality0','asBetweennessCentrality1','asBetweennessCentrality2',
    'asClosenessCentrality0', 'asClosenessCentrality1', 'asClosenessCentrality2',
    'asEigenvectorCentrality0', 'asEigenvectorCentrality1', 'asEigenvectorCentrality2',
    'asClusteringCoefficient0','asClusteringCoefficient1','asClusteringCoefficient2',
    'asSquareClustering0', 'asSquareClustering1', 'asSquareClustering2',
    # 'asRouterNumber0','asRouterNumber1','asRouterNumber2',
    "asAverageNeighborDegree0", "asAverageNeighborDegree1", "asAverageNeighborDegree2",
    # "asMaxCliqueSize0", "asMaxCliqueSize1", "asMaxCliqueSize2",
    "asTrianglesClustering0", "asTrianglesClustering1", "asTrianglesClustering2",
    # 'ixp',
    'label'
]
pima = pd.read_csv("reGenerateSamples.csv", header=None, usecols=[
        4,5,6,
        7,8,9,
        10,11,12,
        13,14,
        15,16,17,
        18,19,20,
        21,22,23,
        24,25,26,
        27,28,29,
        30,31,32,
        33,34,35,
        36,37,38,
        39
        # 39,40,41,
        # 42,43,44,
        # 45,
        
        ],names=featureNames)

from sklearn.model_selection import train_test_split

feature_cols = featureNames[0:-1]


X = pima[feature_cols] # Features
y = pima.label # Target variable

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) # 70% training and 30% test


#Import Random Forest Model
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

# import seaborn as sns
from pprint import pprint


count=1
i=0
accuracylist=[]
while i< count:
    clf=RandomForestClassifier(n_estimators=100, max_depth=10,oob_score=True)
    #Train the model using the training sets y_pred=clf.predict(X_test)
    clf.fit(X_train,y_train)
    y_pred=clf.predict(X_test)
    CM = confusion_matrix(y_test, y_pred)
    TN = CM[0][0]
    FN = CM[1][0]
    TP = CM[1][1]
    FP = CM[0][1]
    accuracylist.append(metrics.accuracy_score(y_test, y_pred))
    i+=1



print(max(accuracylist))
# print(clf.oob_score_)
# print("Parameters:")
# print(clf.get_params())


print("FPR:",FP/(FP+TN))
print("Recall:",metrics.recall_score(y_test, y_pred))
print("Precision:",metrics.precision_score(y_test, y_pred))
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("F1-score:",metrics.f1_score(y_test, y_pred,average='macro'))
