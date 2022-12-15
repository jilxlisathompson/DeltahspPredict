from data_preparation import *
from sklearn.model_selection import train_test_split, LeaveOneOut
from sklearn.model_selection import cross_val_score, KFold, GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE


def perform_leave_one_out_cv(df: pd.DataFrame, hansen_parameter: str):
    # create list of features
    feature_list = df.keys().values.tolist()
    # TODO may need to remove unnecessary columns from feature list ^(feature_list)
    # assign x and y
    X = df.loc[:, feature_list]
    y = df[hansen_parameter] # TODO may need to specify column numbers
    # define cross validation method
    cv = LeaveOneOut()
    # build multiple linear regression model
    model = LinearRegression()
    # use looCV to evaluate model
    scores = cross_val_score(model, X, y, scoring='neg_mean_absolute_error',
                             cv=cv, n_jobs=-1)
    pass





def loocv_for_model_selection():
    # create list of features
    # create cross validation scheme, n_splits = N (number of instances
    # specify hyper parameter range
    # specify model
    # set up gridsearchCV
    # fit model
    # get cv results
    # plot cv results
    pass


def loocv_final_model():

    # fit model with optimal number of reatures
    # predict


    # get name of features
    pass


def perform_recursive_feature_elimination():
    # set up RFE
    # fit
    # return model
    pass
