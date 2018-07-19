#Operadores e Tipos de Variáveis

##Declarando Variáveis

``` python

  # nome-da-variável = valor

  a = 1             #inteiro
  b = 1.0           #real
  c = True          #booleano
  # True/False sempre com a primeira letra maiúscula

  d = "Olá mundo!"  #string
  e = 'Olá mundo!'  #string
  f = [1,2,3,4]     #lista
```
##Operadores

Operações aritméticos básicas:

``` python
  1 + 1   # => 2
  2 - 1   # => 1
  8 * 10  # => 80
  40 / 2  # => 20.0

```
*Toda* divisão retorna um real.

Divisão arredondada (floor division):

``` python
  5 // 3      # => 1
  5.0 // 3.0  # => 1.0
  -5 // 3     # => -2
  5.0 // 3    # => 1.0

```
Retorna o *menor* inteiro mais próximo do valor

Divisão inteira:

``` python
  7 % 3     # => 1
```

Exponenciação:

``` python
  7 ** 2      # => 49
  49 ** 0.5   # => 7.0
```

Operadores Booleanos:

``` python
  not True        # => False
  not False       # => True

  True or False   # => True
  True or True    # => True
  False or True   # => True
  False or False  # => False

  True and True   # => True
  True and False  # => False
  False and True  # => False
  False and False # => False
```

Operadores de comparação:

``` python
  2 == 4 / 2    # => True
  2 == 2        # => True
  2 == 1        # => False

  2 != 1        # => True
  2 != 2        # => False

  1 < 10        # => True
  10 < 1        # => False
  10 > 1        # => True
  1 > 10        # => False
  1 >= 10       # => False
  1 <= 10       # => True

  a = [1,2,3]   
  b = a         
  b is a        # => True
```

== vs. is:

``` python
  a = [1,2,3]   
  b = a         
  b is a        # => True
  b == a        # => True

  b = [1,2,3]
  b is a        # => False, porque não se refere ao mesmo objeto
  b == a        # => True
```
