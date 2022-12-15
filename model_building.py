import pandas as pd
import statsmodels.api as sm
import data_preparation
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
from sklearn.model_selection import KFold, GridSearchCV
from sklearn.model_selection import LeaveOneOut


def kfold_cv_as_loocv(df: pd.DataFrame, hansen_parameter: str):
    # divide df into feature list
    features_list = df.keys().values.tolist()
    # TODO remove unnecessary features
    # instantiate X
    X = df.loc[:, features_list]
    # instantiate y -- N.B. may need to remove
    y = df[hansen_parameter]
    # number of splits for cv
    n_splits = len(y)
    # creating Kfold object
    cv = LeaveOneOut()
    # cv = KFold(n_splits=n_splits, shuffle=True, random_state=42)
    # since this is leave one number of folds = number of instances - 1
    hyper_params = [{"n_features_to_select": list(range(2, 40))}]
    # TODO develop understanding of this variable in order to be accurate
    # specify model
    lm = LinearRegression()
    lm.fit(X, y)
    rfe = RFE(lm)

    # setting up GridSearch CV
    model_cv = GridSearchCV(estimator=rfe,
                            param_grid=hyper_params,
                            scoring="neg_mean_squared_error",
                            cv=cv)
    model_cv.fit(X, y)

    # get cv results
    cv_results = pd.Dataframe(model_cv.cv_results_)
    cv_params = model_cv.best_params_

    return cv_results, cv_params


def get_final_model():
    # get optimal features
    # perform regression
    # set up RFE
    # predict
    pass


def print_params():
    pass


def gaussian_process_regressio():
    pass
