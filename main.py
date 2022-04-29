try:
    print(x)
except NameError:
    print("Bu harf stringa olinmagan")
try:
    abc = abc
    print(abc)
except NameError:
    print("ozini oziga tenglab bolamydi")
try:
    a = 4
    b = 0
    all = a/b
except ZeroDivisionError:
    print('4 ni 0 ga bolib bolamydi')
try:
    print(d/4)
except NameError:
    print("harfni raqamga bolib bolmaydi")
