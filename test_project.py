import pytest
from project import fitting, printing, save


def main():
    test_fitting()
    test_printing()
    test_save()


def test_fitting():
    with pytest.raises(BaseException):
        fitting(x, y, regressor)


def test_printing():
    with pytest.raises(BaseException):
        printing(y, y_pred, regressor)


def test_save():
    with pytest.raises(BaseException):
        save(regressor, path='model.pkl')


if __name__ == "__main__":
    main()