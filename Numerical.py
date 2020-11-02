# ------------------------------------------------------------------------------------------------
import logging as lg                                            
import numpy as np
# ------------------------------------------------------------------------------------------------

# Нахождение корней функции на определённом диапозоне
# Метод Ньютона (касательных)
# Функция, его производная, начало и конец, точность, вернуть кол-во шагов
def Tangent_Method(F, dF, A = 0, B = 1, E = 0.01, Step = False):
    X, I = ((A + B) / 2), 0                                     # Назодим первую X
    while (abs(F(X)) > E):                                      # Проверка X при определённой точности
        I += 1                                                  # Счётчик
        X = X - (F(X) / dF(X))                                  # Находим след Xi
    if(Step): return [X, I]                                     # Возвращаем значение корня и кол-во шагов
    else: return X                                              # Возвращаем значение корня

# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------

# Нахождение корней функции на определённом диапозоне
# Метод половинного деления
# Функция, начало, конец, точность, увиличение мощности, смещение, вернуть кол-во шагов
def Half_Division(F, A = 0, B = 1, E = 0.01, K1 = 1, K2 = 0, Step = False):
    S , I = abs(A - B), 0                                       # Узнаём длину, счётчик в нулевой момент времени
    while ( S > E ):                                            # Цикл нахождения корня
        I += 1                                                  # Счётчик
        C = (A + B) / 2                                         # Находим С (середину)
        # Проверка, откинуть левую или правую часть в случае f(x1) * f(x2) < 0
        if( ( ( F(A) * K1 ) + K2 ) * ( ( F(C) * K1 ) + K2 ) > 0): A = C
        else: B = C
        S = abs(A - B)                                          # Длина отрезка
    if(Step): return [( (A + B) / 2 ), I]                       # Возвращаем значение корня и кол-во шагов
    else: return ( (A + B) / 2 )                                # Возвращаем значение корня

# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------

# Определитель матрицы
# Принимает матрицу, способ нахождения определителя, допустимая точность 
def Det(M, Method = "default", E = 0.01):

# ------------------------------------------------------------------------------------------------

    # Общий случай нахождения определителя
    def _Det_(Ms):

        # Порядок матрицы
        Ls = len(Ms)

        # Случай с одномерной матрицей
        if(Ls == 1): return Ms
    
        # Случай с двухмерной матрицей
        elif(Ls == 2): return Ms[0][0] * Ms[1][1] - Ms[1][0] * Ms[0][1]
    
        # Случай с n-мерной матрицей
        else:
            DET = 0                                             # Резервируем переменную для определителя
            for K in range(Ls):                                 # Считае миноры
                Mi = []                                         # Резервируем переменную для матрицы
                for Y in range(1,Ls):                           # Считаем определители без 1-ой строки
                    Mi.append([])                               # Создаём i-ую строку
                    for X in range(Ls):                         # Считаем определитель без j-ого столбца
                        if(X != K):                             # Проверка столбца
                            Mi[Y-1].append(Ms[Y][X])            # Заполняем матрицу
                        
                # Считаем определитель без i строки и j-ого столбца
                # и умножаем на алгебраическое дополнение и порядок
                DET += Ms[0][K] * _Det_(Mi) * ((-1) ** (K+2))
    
            # Возвращаем результат  
            return DET
# ------------------------------------------------------------------------------------------------

    # Нахожнение определителя путём эквиволентных преобразований 
    def _Det_Triangle(M):

        L = len(M)                                              # Порядок матрицы
        DET = -1                                                # Первоначальный знак определителя
        
        for k in range(L):                                      # Проходим по всем строкам с индексом k  
            
            # --------- --------- СВЕДЕНИЕ К ТРЕУГОЛЬНОЙ МАТРИЦЕ --------- ---------
            if (abs(M[k][k]) <= E):                             # Проверка приближения числа к 0 на главной линии
               n = k + 1                                        # Счётчик
               while(abs(M[n][k]) <= E): n += 1                 # Находим строку для перестановки
               M_Bubble = M[k]; M[k] = M[n]; M[n] = M_Bubble    # Переставляем строки методом пузырика
               DET = -DET                                       # Меняем знак определителя

            for i in range(L):                                  # Проходим по всем строкам с индексом i                                                      
                if (i > k):                                     # Если строка i ниже строки k
                    g = M[i][k] / M[k][k]                       # Находим отношение g                                                      
                    for j in range(L):                          # Проходим по j-ым элементам строки                                                    
                        if (j >= k):                            # Достаточное условие                                           
                            M[i][j] = M[i][j] - (g * M[k][j])   # Демонтаж
            # ------------------ ------------------ ------------------ ------------------

        # Находим определитель с помощью перемножения главной строки
        for i in range(L): DET *= M[i][i]    
        
        # Возвращаем значение и умножаем его на соответствующий знак
        return DET                                              

# ------------------------------------------------------------------------------------------------

    # Порядок матрицы
    L = len(M)
   
    # Проверка квадратной матрицы и правильности данных
    if(L > 1):                                                  # Если матрица размерности больше чем 1
        for i in range(L):                                      # Перебираем все строки
            if(len(M[i]) != L):                                 # Если в строки значений меньше или больше чем кол-во строк
                lg.error("\t <Det> \t Ошибка определителя: матрица не является квадратной!!!")
                return 0                                        # Значит матрица не квадратная или заполнена неправильно
    
# ------------------------------------------------------------------------------------------------

    # Случай с одномерной матрицей
    if(L == 1): return M[0]

    # Случай с двухмерной матрицей
    elif(L == 2): return M[0][0] * M[1][1] - M[1][0] * M[0][1]

    # Случай с n-мерной матрицей
    else:
        if(Method == "default"):    return round( _Det_(M),          int( abs( np.log10(E) ) ) )
        if(Method == "triangle"):   return round( _Det_Triangle(M),  int( abs( np.log10(E) ) ) )
        else:
            lg.error("\t <Det> \t Ошибка параметра: " + Method + " не существует!!!")
            return 0
       
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
       
# Нахожнение корней в системе уровнений методом Гаусса
# Принимает матрицу коэф уровнений, ответы уровнений и допустимая точность
def Gauss(X, Y, E = 0.01):

    L = len(X)                                              # Порядок матрицы
    Xs = []                                                 # Резервируем список для хранения корней

    # --------- --------- СВЕДЕНИЕ К ТРЕУГОЛЬНОЙ МАТРИЦЕ --------- ---------
    for k in range(L):                                      # Проходим по всем строкам с индексом k  
        
        if (abs(X[k][k]) <= E):                             # Проверка приближения числа к 0 на главной линии
           n = k + 1                                        # Счётчик
           while(abs(X[n][k]) <= E): n += 1                 # Находим строку для перестановки
           M_Bubble = X[k]; X[k] = X[n]; X[n] = M_Bubble    # Переставляем строки уравнений методом пузырика
           M_Bubble = Y[k]; Y[k] = Y[n]; Y[n] = M_Bubble    # Переставляем строки ответов методом пузырика
           
        for i in range(L):                                  # Проходим по всем строкам с индексом i                                                      
            if (i > k):                                     # Если строка i ниже строки k
                g = X[i][k] / X[k][k]                       # Находим отношение g     
                Y[i] = Y[i] - (g * Y[k])                    # Преобразование
                for j in range(L):                          # Проходим по j-ым элементам строки                                                    
                    if (j >= k):                            # Достаточное условие                                           
                        X[i][j] = X[i][j] - (g * X[k][j])   # Демонтаж
      # ------------------ ------------------ ------------------ ------------------

    for y in range(L)[::-1]:                                # Поиск корней с последней строки
        N = len(Xs)                                         # Узнаём, сколько корней известно
        Z = [X[y][len(X[y])-x-1]*Xs[x] for x in range(N) ]  # Умнажаем коэф на известные корни
        for x in range(len(Z)): Y[y] -= Z[x]                # Отнимаем от результата произведение известных корней и коэф
        Xs.append( round(Y[y] / X[y][y] , int( abs( np.log10(E)))))    
         
    # Возвращаем список корней системы уровнений
    return Xs          
    
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------

