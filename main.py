from MyMathModule import MyMathModule as mmm


numbers = mmm.read_csv_data_to_float("test2.csv")
mean = mmm.mean(numbers)
variance = mmm.variance(numbers, mean)
std_der = mmm.std_derivation(variance)
print("moyenne: {:10.2f}".format(mean))
print("variance: \t{:10.2f}".format(variance))
print("ecart-type: {:7.2f}".format(std_der))
