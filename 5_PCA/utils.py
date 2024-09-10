import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
import warnings
from sklearn.base import BaseEstimator, ClassifierMixin, clone


def delete_from_substring(string):
    index = string.find('(')
    if index != -1:
        return string[:index]
    return string


def split_df(data: pd.DataFrame, n: int, n_col: int):
    dataframes = {}
    for i in range(n):
        col_first = i * n_col
        col_last = col_first + n_col

        df = data.iloc[:, col_first:col_last]
        dataframes[f'X_{i+1}'] = df

    return dataframes


def columns_df(df: pd.DataFrame):
    int_columns = list(df.select_dtypes(include='int').columns)
    float_columns = list(df.select_dtypes(include='float').columns)
    object_columns = list(df.select_dtypes(include='object').columns)
    numerical_columns = int_columns + float_columns

    print('Shape:', df.shape)
    print('Numerical features: ', len(numerical_columns))
    print('Categorical features: ', len(object_columns))

    return int_columns, float_columns, object_columns, numerical_columns


def most_frequent(row):
    values, counts = np.unique(row, return_counts=True)
    max_count_index = np.argmax(counts)
    return values[max_count_index]


warnings.filterwarnings("ignore", message="X does not have valid feature names, but NearestNeighbors was fitted with "
                                          "feature names")



