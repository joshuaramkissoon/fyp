import pandas as pd
import numpy as np
from statistics import stdev,mean
import os


def getFormattedLabel(label, addText):
    split = label.split('/', 2)
    formatted = '/'.join(split[:2]) + '-' + addText + '/' + split[-1]
    return formatted

def displayDataframe(df):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(df.values)   


def readHDF(path):
    return pd.read_hdf(
                path,
                "df_with_missing",
            )

def writeDataframetoHDF(df, path):
    df.to_hdf(
            path,
            "df_with_missing",
            format="table",
            mode="w",
        )

def writeDataframeToCSV(df, path):
    df.to_csv(path)


def allNan(arr):
    return all(np.isnan(arr))

def removeNanRows(df):
    return df.dropna(how='all')

def formatLabelledData(folder_path):
    '''
    Remove all empty rows (NaN)
    Write to csv file CollectedData_joshua.csv
    Write to h5 file CollectedData_joshua.h5
    '''
    csv_path = folder_path + '/CollectedData_joshua.csv'
    h5_path = folder_path + '/CollectedData_joshua.h5'
    df_orig = readHDF(h5_path)
    df_new = removeNanRows(df_orig)
    writeDataframeToCSV(df_new, csv_path)
    writeDataframetoHDF(df_new, h5_path)

def getNumberLabelledFrames(df):
    return len(removeNanRows(df).index.values)

def getStdev(arr):
    return stdev(arr)

def getMean(arr):
    return mean(arr)

def normaliseErrors(agg, occ, criteria):
    ''' 
    Agg is a list of aggregate errors
    Occ is a list of occluded errors
    Criteria is the desirable prediction criteria
    '''
    return (np.true_divide(agg,criteria), np.true_divide(occ,criteria))

def getDiameter(insect_id):
    '''
    Returns the diameter for the insect with ID
    '''
    insects = {
        1: 15,
        2: 16,
        3: 15,
        4: 9,
        5: 20
    }
    return insects[insect_id]

def getDesirableCriteria(insect):
    '''
    Desirable criteria is half the diameter of smallest bodypart on insect
    '''
    return getDiameter(insect)/2


def main():
    agg = [3.55]
    occ = [203.15]
    c = getDesirableCriteria(5)
    a, o = normaliseErrors(agg, occ,c)


if __name__ == '__main__':
    main()