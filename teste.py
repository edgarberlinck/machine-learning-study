import my_math
# from my_math import * importa a porra toda, assim não precisa mais digitar my_math
# from my_math import area_quad # mesma coisa, mas importa apenas a função area_quad
# Note que se usamos o import universal podemos fuder com nossa vida pois caso dois pacotes declarem funções com o mesmo nome o que vai valer 
# é a função do último pacote importado

print(my_math.area_quad(5))
print(my_math.area_ret(5,10))
print(my_math.peri_quad(10))
