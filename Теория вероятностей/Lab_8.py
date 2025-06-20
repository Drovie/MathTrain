#Задание 8

#Для трех розничных торговых предприятий определен плановый уровень
#прибыли. Вероятность того, что первое предприятие выполнит план прибыли, равна 90%, 
#для второго она составляет 95%, для третьего 100%. 
#Какова вероятность того, что плановый уровень прибыли будет достигнут: 
#а) всеми предприятиями; б) только двумя предприятиями; в) хотя бы одним предприятием.


#А)Вероятность, что план будет достигнут всеми предприятиями
P_A = 0.9*0.95*1
print("Вероятность, что план будет достигнут всеми предприятиями: ",P_A)

#Б)Вероятность, что план будет достигнут только двумя предприятиями
P_B = 0.9*(1-0.95) + (1-0.9)*0.95
print("Вероятность, что план будет достигнут только двумя предприятиями: ",P_B)

#В)Вероятность, что план будет достигнут хотя бы одним предприятием
P_C = 1# так как третье предприятие выполняет план в 100% случаев
print("Вероятность, что план будет достигнут хотя бы одним предприятием: ",P_C)