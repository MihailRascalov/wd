#Napisz skrypt, który policzy i wyświetli następujące wyrażenia:
#e^10
#6^sqrt(ln(5+sin^2 8))
#|3.55|
#|4.80|

import math

print("e^10 = " + str(round(math.pow((math.e), 10), 2)))
print("(ln(5+(sin(8))^2)^(1/6)) = " + str(math.log(5 + math.pow(math.sin(8), 2))**1/6))
print("|3,55| = " + str(abs(3.55)))
print("|4.80| = " + str(abs(4.80)))