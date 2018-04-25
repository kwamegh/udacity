#!/usr/bin/python 

""" 
    This is the code to accompany the Lesson 2 (Support Vector Machine) mini-project. 

    Use a Support Vector Machine Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
   Chris has label 1
"""

# modules 
import sys
import time
sys.path.append("../lib/tools/") 
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###

# Create SVC classifier
# clf = SVC(kernel="linear") # linear kernel 

## RBF kernel (Radial Basis Function) 
# rbf kernel , C (say, 10.0, 100., 1000., and 10000.)
#clf = SVC(kernel="rbf") 
#clf = SVC(kernel="rbf", C=10.0)
#clf = SVC(kernel="rbf", C=100.0)
#clf = SVC(kernel="rbf", C=1000.0)
clf = SVC(kernel="rbf", C=10000.0)

# to speed up classifier, use less training datasets
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

t0=time.time()
clf.fit(features_train, labels_train)
print "\ntraining time:", round(time.time()-t0, 3), "s"

# Classify test data with the classifier
t1=time.time()
target_pred=clf.predict(features_test)
print "predicting time:", round(time.time()-t1, 3), "s"

# Calculate Accuracy Rate of label_test manually
accuracy=accuracy_score(labels_test, target_pred)
print "\naccuracy rate: " + str(accuracy)

# extract predictions - 10, 26, 50
lst = [10,26,50]

for i in range(len(lst)):
	answer = target_pred[lst[i]]
	print "prediction of " + str(lst[i])+ ": " + str(answer)

# How Many Emails of a specific author is predicted - this case Chris ("1")
count = 0
for i in range(len(target_pred)):
	if (target_pred[i] == 1):
		count +=1
	
print count
#print target_pred[8:20]
#########################################################