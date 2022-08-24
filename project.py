import sys
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


def main():

    # Since it's a very small dataset, we will train model with all available data
    dataset = pd.read_csv('job_search.csv')
    x = dataset.iloc[:, :-1]
    y = dataset.iloc[:, -1]

    # Make predictions using the testing set
    regressor = LinearRegression()
    y_pred = fitting(x, y, regressor)

    # Print coefficients and R^2 (coefficient of determination)
    printing(y, y_pred, regressor)

    # Save the model
    path = input("Default path: 'model.pkl'\nChoose the path: ").strip()
    if path.split('.')[-1] != 'pkl':
        sys.exit('Not a pickle file, please save file in the format <file name>.pkl')
    else:
        save(regressor, path)


def fitting(x, y, regressor):
    ''' Fitting model with training data '''
    regressor.fit(x, y)
    return regressor.predict(x)


def printing(y, y_pred, regressor):
    '''
    Print coefficients and R^2 (coefficient of determination)
    '''

    # The coefficients
    print("Coefficients:\n", regressor.coef_)

    # The coefficient of determination: 1 is perfect prediction
    print("Coefficient of determination: %.2f" % r2_score(y, y_pred))


def save(regressor, path='model.pkl'):
    ''' Saving the model '''
    pickle.dump(regressor, open(path, 'wb'))


if __name__ == '__main__':
    main()