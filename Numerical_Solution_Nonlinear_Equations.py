from Numerical import *
#  Графики функции http://yotx.ru/


def _F(X): return (5 * (X**3) - (X ** 2) - 20 * X + 4)
def _dF(X): return (15 * (X ** 2) - 2 * X - 20)

# Главный метод
if __name__ == '__main__':
    print("Метод половинного деления: ", Half_Division( -10, 0, _F, E=0.00001 ) )
    print("Метод Ньютона: ", Tangent_Method( -10, 0, _F, _dF , E=0.00001 ) )





