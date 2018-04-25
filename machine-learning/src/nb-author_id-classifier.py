#!/usr/bin/python 

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
   Chris has label 1
"""

# modules 
import sys
import time
sys.path.append("../lib/tools/") 
from email_preprocess import preprocess
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

# Create Naive Bayes classifier
clf=GaussianNB()
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

#########################################################