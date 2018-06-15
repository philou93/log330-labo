from MyMathModule import MyMathModule as mmm
from Reader import MyReader as mr


# Partie pour le TP1
# numbers = mr.read_csv_data_to_float("test_tp1.csv")
# mean = mmm.mean(numbers)
# variance = mmm.variance(numbers, mean)
# std_der = mmm.std_derivation(variance)
# print("moyenne: {:10.2f}".format(mean))
# print("variance: \t{:10.2f}".format(variance))
# print("ecart-type: {:7.2f}".format(std_der))

# Partie pour le TP2
numbers = mr.read_csv_data_to_float("test_tp2.csv")
corelation = mmm.caculateCorelation(numbers)
print("corrélation: {:0.6f}".format(corelation))
print(mmm.interpreteCorelationInWord(corelation))

