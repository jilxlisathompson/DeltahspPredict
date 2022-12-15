from yellowbrick.model_selection import RFECV
from data_reading import *
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import  LeaveOneOut
from sklearn.model_selection import cross_val_score, KFold, GridSearchCV

def recursive_feature_elimination_cv(df, hansen_parameter: str) -> None:

    # get data
    # create list of features
    feature_list = df.keys().values.tolist()
    # TODO may need to remove unnecessary columns from feature list ^(feature_list)
    # instantiate X
    # instantiate y
    X = df.loc[:, feature_list]
    y = df[hansen_parameter]  # TODO may need to specify column numbers
    # define cross validation method
    visualiser = RFECV(LinearRegression())
    # performing RFE with LinearRegression()
    visualiser.fit(X, y)
    visualiser.show()
    # use yellowbrick visualiser

    return None

def feature_importance():
    pass
