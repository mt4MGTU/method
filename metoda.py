# coding: utf-8

import math

# к методу 1
#

def MeanValueOfInfluenceQuantity(influenceQuantity1,influenceQuantity2):  # MeanValueOfInfluenceQuantity - мат.ожидание влияющих величин,
    # InfluenceQuantity - влияющая величина, 1 - верхняя граница, 2 - нижняя граница
    return 0.5 * (influenceQuantity1 + influenceQuantity2)

def MeanValueOfBasicErr(ValueOfBasicErr):  # MeanValueOfBasicErr - мат. ожидание допускаемых значений систематической составляющей основной погрешности
    # ValueOfBasicErr - предел допускаемых значений систематической составляющей основной погрешности
    return ValueOfBasicErr

def MeanValue(meanValueOfInfluenceQuantity, meanValueOfBasicErr, coefSF, valueOfInfluenceQuantity, influenceQuantity1,influenceQuantity2):
    # MeanValue - математическое ожидание статической составляющей,
    # CoefSF - номинальный коэффициент влияния j-й влияющей величины на систематическую составляющую погрешности СИ
    # ValueOfInfluenceQuantity - нормальное значение j-й влияющей величины
    # Sigma - СКО от влияющей величины
    sigma = round((influenceQuantity1 - influenceQuantity2) / math.sqrt(12), 3)
    return round(meanValueOfBasicErr + coefSF * ((meanValueOfInfluenceQuantity - valueOfInfluenceQuantity) ** 2) + coefSF * sigma ** 2, 3), sigma

def Dispersion(coefSF, valueOfInfluenceQuantity, meanValueOfInfluenceQuantity, sigma, sigmaP, nominalPrice,limitOfAllowedValues):  # Dispersion - дисперсия статической составляющей погрешности
    # SigmaP - предел допускаемых значений СКО случайной cоставляющей основной погрешности
    # NominalPrice - номинальная цена единицы наименьшего разряда кода
    # SigmaOfBasicErr - сигма от предела допускаемых значений систематической составляющей основной погрешности
    # LimitOfAllowedValues - предел допускаемых значений систематической составляющей основной погрешности
    sigmaOfBasicErr = limitOfAllowedValues / math.sqrt(3)
    return round(sigmaOfBasicErr ** 2 + (2 * coefSF * (meanValueOfInfluenceQuantity - valueOfInfluenceQuantity)) ** 2 * sigma ** 2 + 1.6 * coefSF ** 2 * sigma ** 4 + sigmaP ** 2 + nominalPrice ** 2 / 12, 3)

def IntervalOfErr(meanValue, dispersion, p, dispersionOfDinamic=0):  # IntervalOfError -границы интервальной оценки
    coefK = 5 * (p - 0.5)
    # DispersionOfDinamic = 0 #т.к. не динамическая
    sigmaOfMeasuring = round(math.sqrt(dispersion + dispersionOfDinamic), 3)
    intervalOfErr1 = round(meanValue + coefK * sigmaOfMeasuring, 3)
    intervalOfErr2 = round(meanValue - coefK * sigmaOfMeasuring, 3)
    return intervalOfErr1, intervalOfErr2

# # к методу 2
#
# def SDOfBasicErr(error): # SDOfBasicErr - СКО основной погрешности
# # Error - предел допускаемого значения основной погрешности i-го блока ИИС
#     return math.fabs(error)/1.7
#
# def ValueOfAdditionalErr(diffOfInfluenceQuantity, coef, influenceQuantity, valueOfInfluenceQuantity, errOfInfluenceQuantity): #ValueOfAdditionalErr - наибольшее возможное значение дополнительной погрешности
# # DiffOfInfluenceQuantity - приращение j-й влияющей величины, для которой нормирована МХ; Coef - коэф-т;
# #InfluenceQuantity - влияющая вел-на;ValueOfInfluenceQuantity - значение влияющей вел-ны;
# # ErrOfInfluenceQuantity - допускаемое изменение  погрешности i-го блока ИИС, вызванное отклонением j-й влияющей величины от норм. знач-я
#     if influenceQuantity == valueOfInfluenceQuantity:
#         coef = 0
#     elif influenceQuantity != valueOfInfluenceQuantity:
#         coef = 1
#     elif errOfInfluenceQuantity == diffOfInfluenceQuantity: #!!!!!!!!!!!!!!!!!!!!!!!!!!1КАЖИСЬ ВСЕ РАВНО НЕ ПОНЯТНО
#         coef = math.fabs(influenceQuantity-valueOfInfluenceQuantity)/diffOfInfluenceQuantity
#     return errOfInfluenceQuantity*coef
#
# def SDOfAdditionalErrInfluenceQuantity(valueOfAdditionalErr): # SDOfAdditionalErrInfluenceQuantity - СКО дополнительной погрешности i-го блока ИИС от j-й влияющей величины
# #ValueOfAdditionalErr - наибольшее возможное значение дополнительной погрешности
#     return math.fabs(valueOfAdditionalErr)/1.7
#
# def SDOfRandomErr(sdOfBasicErr, numbOfInfluenceQuantity, sdOfAdditionalErrInfluenceQuantity): #SDOfRandomErr - СКО случайной погрешности блока;
# #  NumbOfInfluenceQuantity - количество влияющих величин
# #sdOfBasicErr - СКО дополнительной погрешности i-го блока ИИС от j-й влияющей величины
#     for i in range(numbOfInfluenceQuantity):
#         sdOfBasicErr += 2 #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!НА ЧТО УВЕЛИЧИВАЕТСЯ?!
#     return math.sqrt(sdOfAdditionalErrInfluenceQuantity**2+ sdOfBasicErr) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!ОПЯТЬ НЕПОНЯТНО КАК СУММУ СЧИТАТЬ
#
# def SDOfRandomErrOfIK(numbOfBlocks, sdOfRandomErr): #SDOfRandomErrOfIK - СКО случайной погрешности ИК
# #  NumbOfBlocks - количество блоков, входящих в состав ИК
#     for i in range(numbOfBlocks):
#         sdOfRandomErr += 2 #НЕПОНЯТНО ОПЯТЬ,ТОЖЕ СУММА
#     return math.sqrt(sdOfRandomErr**2)
#
# def IntervalOfErr2(sdOfRandomErrOfIK, confidProbability): #IntervalOfError2 - границы интервала погрешности ИК;
# # ConfidProbability - вероятность (P)
#     return sdOfRandomErrOfIK*confidProbability

# тело проограммы

# metod = int(input()) #выбор метода для расчета
metod = 1
#
if metod == 1:
    print('Расчет по методу 1')  # отладка
    #influenceQuantity1 = int(input('Введите влияющую величину 1 (верхняя граница)'))
    influenceQuantity1 = 30
    #influenceQuantity2 = int(input('Введите влияющую величину 2 (нижняя граница)'))
    influenceQuantity2 = 60
    meanValueOfInfluenceQuantity = MeanValueOfInfluenceQuantity(influenceQuantity1, influenceQuantity2)
    #valueOfBasicErr = int(input('Введите предел допускаемых значений систематической составляющей основной погрешности'))
    valueOfBasicErr = 0
    meanValueOfBasicErr = MeanValueOfBasicErr(valueOfBasicErr)
    print('Значение мат. ожидания допускаемых значений систематической составляющей основной погрешности',meanValueOfBasicErr)
    #coefSF = int(input('Введите номинальный коэффициент влияния влияющей величины на систематическую погрешность СИ'))
    coefSF = 0.001
    #ValueOfInfluenceQuantity = int(input('Введите нормальное значение влияющей величины'))
    valueOfInfluenceQuantity = 20
    #meanValue, sigma = MeanValue(meanValueOfInfluenceQuantity, meanValueOfBasicErr, coefSF,valueOfInfluenceQuantity, influenceQuantity1[i], influenceQuantity2[3])
    meanValue, sigma = MeanValue(meanValueOfInfluenceQuantity, meanValueOfBasicErr, coefSF, valueOfInfluenceQuantity, influenceQuantity1,influenceQuantity2)
    print('Значение математического ожидания статической составляющей', meanValue, ". Sigma: ", sigma)
    # sigmaP = int(input('Введите предел допускаемых значений СКО случайной составляющей основной погрешности'))
    sigmaP = 0.3
    # nominalPrice = int(input('Введите номинальную цену единицы наименьшего разряда кода'))
    nominalPrice = 1
    # limitOfAllowedValues = int(input('Введите предел допускаемых значений систематической составляющей основной погрешности'))
    limitOfAllowedValues = 1
    dispersion = Dispersion(coefSF, valueOfInfluenceQuantity, meanValueOfInfluenceQuantity, sigma, sigmaP,nominalPrice, limitOfAllowedValues)
    print('Значение дисперсии статической составляющей погрешности', dispersion)
    # p = int(input('Введите вероятность'))
    p = 0.9
    intervalOfErr1, intervalOfErr2 = IntervalOfErr(meanValue, dispersion, p)
    print('Границы интервальной оценки: от ', intervalOfErr2, " до ", intervalOfErr1)


    # elif metod == 2:
    #     ##Error = int(input('Введите предел допускаемого значения основной погрешности i - го блока ИИС'))
    #     error = 1
    #     sdOfBasicErr = SDOfBasicErr(error)
    #     print('Значение СКО основной погрешности', sdOfBasicErr)
    #
    #     ##DiffOfInfluenceQuantity = int(input('Введите приращение j-й влияющей величины, для которой нормирована МХ'))
    #     diffOfInfluenceQuantity = 4
    #     ##Coef = int(input('Введите значение коэффициента'))
    #     coef = 0.5
    #     ##InfluenceQuantity = int(input('Введите влияющую величину'))
    #     influenceQuantity = 1
    #     ##ValueOfInfluenceQuantity = int(input('Введите значение влияющей величины'))
    #     valueOfInfluenceQuantity = 7
    #     ##ErrOfInfluenceQuantity = int(input('Введите допускаемое изменение погрешности блока ИИС, вызванное отклонением влияющей величины от норм.знач - я'))
    #     errOfInfluenceQuantity = 1
    #     valueOfAdditionalErr = ValueOfAdditionalErr(diffOfInfluenceQuantity, coef, influenceQuantity, valueOfInfluenceQuantity, errOfInfluenceQuantity)
    #     print('Значение наибольшего возможного значения дополнительной погрешности', valueOfAdditionalErr)
    #
    #     # вроде не надо,описала лишнего
    #     # sdOfAdditionalErrInfluenceQuantity = SDOfAdditionalErrInfluenceQuantity(valueOfAdditionalErr)
    #     # print('Значение СКО дополнительной погрешности от влияющих величин', sdOfAdditionalErrInfluenceQuantity)
    #
    #     sdOfAdditionalErrInfluenceQuantity = SDOfAdditionalErrInfluenceQuantity(valueOfAdditionalErr)
    #     print('Значение СКО дополнительной погрешности i-го блока ИИС от j-й влияющей величины', sdOfAdditionalErrInfluenceQuantity)
    #     ##NumbOfInfluenceQuantity = int(input('Введите количесво влияющих величин'))
    #     numbOfInfluenceQuantity = 3
    #     sdOfRandomErr = SDOfRandomErr(sdOfBasicErr, numbOfInfluenceQuantity,sdOfAdditionalErrInfluenceQuantity)
    #     print('Значение СКО случайной погрешности блока', sdOfRandomErr)
    #     ##NumbOfBlocks = int(input('Введите количество блоков, входящих в состав ИК'))
    #     numbOfBlocks = 2
    #     sdOfRandomErrOfIK = SDOfRandomErrOfIK(numbOfBlocks, sdOfRandomErr)
    #     print('Значение СКО случайной погрешности ИК', sdOfRandomErrOfIK)
    #     ##ConfidProbability = int(input('Введите значение вероятности'))
    #     confidProbability = 0.95
    #     intervalOfErr1 = IntervalOfErr2(sdOfRandomErrOfIK, confidProbability)
    #     intervalOfErr2 = IntervalOfErr2(sdOfRandomErrOfIK, confidProbability)
    #     print('Значение границ интервала погрешности ИК', intervalOfErr1,intervalOfErr2 )