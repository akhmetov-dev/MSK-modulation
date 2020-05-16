import math

fs = 2000
inp_msg = list()                                           # Введенное пользователем двоичное сообщение для модуляции и демодуляции
msg = list()                                               # Сообщение, растянутое по всему времени измерения
ts = list()                                                # Временные отсчеты
x0 = list()                                                # Первая синусоида
x1 = list()                                                # Вторая синусоида
mod_msg = list()                                           # Модулированное сообщение
f0 = 10                                                    # Частота первой синусоиды
f1 = 30                                                    # Частота второй синусоиды
i = 0
pi = 3.14                                                  # Число ПИ

fname = input("Input filename :")

try :                                                      # Попытка открыть файл для записи результатов
    fhandler = open(fname, 'w')
except :
    print("Something wrong.")
    quit()

count = int(input("Input length of message: "))            # Количество битов в сообщении, подлежащем модуляции

if count <= 0 : quit

i = 0

while i < count :                                          # Ввод сообщения
    bit = int(input(": "))
    if bit == 0 or bit == 1 :
        inp_msg.append(int(bit))
        i = i + 1
    else :
        print("Incorrect bit.")

print(inp_msg)

i = 0

for bit in inp_msg:                                        # Растягивание сообщения по всему временному отрезку
    while i < fs / len(inp_msg) :
        msg.append(bit)
        i = i + 1
    i = 0

while i < fs :                                             # Получение синусоид, из которых будет смодулирован итоговый сигнал
    if len(ts) < 1 :
        ts.append(1 / fs)
    else :
        ts.append(ts[i - 1] + (1 / fs))
    x0.append(math.sin(2 * pi * f0 * ts[i]))
    x1.append(math.sin(2 * pi * f1 * ts[i]))
    i = i + 1

i = 0

for bit in msg :                                           # Модуляция
    if bit == 1 :
        mod_msg.append(x0[i])
    else :
        mod_msg.append(x1[i])
    i = i + 1

mul1 = list()
mul2 = list()
sub = list()
i = 0

while i < len(x0) :
    mul1.append(mod_msg[i] * x0[i])
    mul2.append(mod_msg[i] * x1[i])
    sub.append(mul1[i] - mul2[i])
    i = i + 1

i = 0
demod = list()
while i < 90 :
    demod.append(0)
    i = i + 1

i = 10
while i < len(sub) :
    demod.append((sub[i - 1] + sub[i - 2] + sub[i - 3] + sub[i - 4] + sub[i - 5] + \
    sub[i - 6] + sub[i - 7] + sub[i - 8] + sub[i - 9] + + sub[i - 10] + \
    sub[i - 11] + sub[i - 12] + sub[i - 13] + sub[i - 14] + sub[i - 15] + \
    sub[i - 16] + sub[i - 17] + sub[i - 18] + sub[i - 19] + sub[i - 20] + \
    sub[i - 21] + sub[i - 22] + sub[i - 23] + sub[i - 24] + sub[i - 25] + \
    sub[i - 26] + sub[i - 27] + sub[i - 28] + sub[i - 29] + sub[i - 30] + \
    sub[i - 31] + sub[i - 32] + sub[i - 33] + sub[i - 34] + sub[i - 35] + \
    sub[i - 36] + sub[i - 37] + sub[i - 38] + sub[i - 39] + sub[i - 40] + \
    sub[i - 41] + sub[i - 42] + sub[i - 43] + sub[i - 44] + sub[i - 45] + \
    sub[i - 46] + sub[i - 47] + sub[i - 48] + sub[i - 49] + sub[i - 50] + \
    sub[i - 51] + sub[i - 52] + sub[i - 53] + sub[i - 54] + sub[i - 55] + \
    sub[i - 56] + sub[i - 57] + sub[i - 58] + sub[i - 59] + sub[i - 60] + \
    sub[i - 61] + sub[i - 62] + sub[i - 63] + sub[i - 64] + sub[i - 65] + \
    sub[i - 66] + sub[i - 27] + sub[i - 68] + sub[i - 69] + sub[i - 70] + \
    sub[i - 71] + sub[i - 72] + sub[i - 73] + sub[i - 74] + sub[i - 75] + \
    sub[i - 76] + sub[i - 77] + sub[i - 78] + sub[i - 79] + sub[i - 80] + \
    sub[i - 81] + sub[i - 82] + sub[i - 83] + sub[i - 84] + sub[i - 85] + \
    sub[i - 86] + sub[i - 87] + sub[i - 88] + sub[i - 89] + sub[i - 90]) / 89)
    i = i + 1

i = 0
demod_msg = list()
while i < len(demod) :
    if demod[i] > 0.2 :
        demod_msg.append(0)
    else :
        demod_msg.append(1)
    i = i + 1

i = 0
while i < len(msg) :
    fhandler.write(str(msg[i]) + " " + str(mod_msg[i]) + " " + str(mul1[i]) + " " + str(mul2[i]) + " " + str(sub[i]) + " " + str(demod[i]) + " " + str(demod_msg[i]) + "\n")
    i = i + 1
