# import scikit learn datasets libraries
from sklearn import datasets
# import the split function using cross validation
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
# importing the svm model
from sklearn.svm import SVC
#  import the metrics for the calculation of accuracy 
from sklearn import metrics

#loads the iris dataset
IRIS = datasets.load_iris()

# create the x and z
X = IRIS.data
z = IRIS.target

#splitting the dataset into training and test data
X_train, X_test, z_train, z_test = train_test_split(X, z, test_size=0.3, random_state=20)

clf = SVC(kernel='rbf')

#model is training with the training sets
clf.fit(X_train, z_train)

#prediction done on test dataset
z_pred = clf.predict(X_test)

# calculating accuracy for the actual and predicted values of test datasets
print("Accuracy of svm with rbf method is:",metrics.accuracy_score(z_test, z_pred))

