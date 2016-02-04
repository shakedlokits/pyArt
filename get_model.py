import pickle
from sklearn import svm
from sklearn.externals import joblib
import numpy as np


def get_model(data, tags, file_name = None):
  '''
  gsts the scikit-learn model.
  if given a file name, saves the model file (.pkl) in this path. to load: clf = joblib.load('file_name.pkl')
  if not, returns a string model. to load: clf = pickle.loads(s)
  '''
    clf = svm.SVC()
    clf.decision_function_shape = "ovr"
    clf.fit(data, tags) 
    
    if file_name is None:
        return pickle.dumps(clf)
        
    else:
        if not file_name.endswith('.pkl') :  file_name = file_name + '.pkl' 
        print 'saving model...'
        joblib.dump(clf, file_name)


'''
data = np.array([[-1, -1 , 3], [-2, -1, 3], [1, 1,-3], [2, 1,3],[1, 2 , 3]])
tags = np.array([1, 1, 2, 2, 2])

s = get_model(data, tags )
clf = pickle.loads(s)
print clf.predict([1, 1, 3])

file_name = 'name'
get_model(data, tags, file_name )
clf = joblib.load('name.pkl')
print clf.predict([1, 1, 3])
'''
