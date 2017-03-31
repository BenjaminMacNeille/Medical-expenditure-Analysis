import pandas as pd
import numpy as np
import sklearn.multioutput
from sklearn import ensemble

class OutpatientClean(object):
    """input raw outpatient data set, output clean df"""

    def __init__(self, df):
        self.df = df

    def filter_negs(self):
        '''
        drop rows with a not ascertained, DK, or refused
        '''
        for col in self.df:
            self.df = self.df[self.df[col] > -2]


    def drop_cols(self):
        '''
        See if EVNTIDX is a key in another table
        EVENTRN read if event round is for the same condition or linked events
        Read about MPCDATA
        OPDATEMM could be interesting for readmission rate
        OPAT Doctor's specialty and medptype -- half are inapplicable
        '''
        self.df = self.df.drop(["DUID","PID", "FFEEIDX", "PANEL", "OPDATEYR", "EVNTIDX", "FFEEIDX","PANEL",
                        "OPDATEYR"], 1)



    def response_columns(self):
        y_start = self.df.columns.get_loc("OPXP14X")
        y_end = self.df.columns.get_loc("OPDTC14X")
        Y = self.df.ix[:,y_start:y_end]
        x_end = self.df.columns.get_loc('OPCCC4X')
        X = self.df[list(self.df.columns[:x_end])]
        return Y, X

    def dummy_cols(X):

        '''
        DRSPLTY, OPAT Doctor's specialty, and medptype -- half are inapplicable

        '''
        X_dummies = pd.concat([pd.get_dummies(X[col]) for col in X], axis=1, keys=X.columns)

        return X_dummies

    def muliple_regressor(X_dummies,Y):
        multi = multioutput.MultiOutputRegressor(ensemble.RandomForestRegressor(random_state=0),n_jobs = -1)
