# Strings e Listas

Strings podem ser declaradas tanto com "" ou ''

## Concatenando Strings

Strings podem ser concatenadas de ambas as formas abaixo:

``` python

  "Olá " + "mundo!"   # => "Olá mundo!"
  "Olá " "mundo!"     # => "Olá mundo!"
```

## Interpolando strings

Strings podem ser interpoladas com o .format()

``` python

  "Eu quero {}!!!".format("café")

  "{} quer {}!!!".format("Fulana", "café")

  "{0}!{0}!{0}!".format("café")

  "{0}!{1}!{2}!".format("uno", "dos", "tres")

  "{nome}, son of {pai}, is not impressed!".format(nome = "Gimli", pai = "Gloin")
```

## Métodos de string

### enumerate()

Retorna um objeto *enumerate* baseado na string

``` python

  enumerate("AAAAAAAAAAAAAAAAAAAA")
  # retorna o objeto =>
  # <enumerate object at 0x000001AD86D5B798>
```

### .lower() e .upper()

Retorna a string em caixa alto ou baixa

``` python

  "AaaaAaaAA!".lower() # => "aaaaaaaaa!"

  "AaaaAaaAA!".upper() # => "AAAAAAAAA!"
```

### .split()

Retorna uma lista com  cada palavra na string

``` python

  "Eu quero café".split()
  # ["Eu", "quero", "café"]
```

### .join()

Retorna uma string com as strings de uma lista

``` python

  " ".join(["Eu", "quero", "café"])
  # "Eu quero café"
  # a string " " fica entre as outras
```

### .find()

Retorna o índice de uma string dentro de outras

``` python

  "Eu quero café".find("q") # => 3
```

### .replace()

Substitui um trecho de uma string por outro

``` python

  "Eu quero café".replace("café", "amor") # => 3
```

## Listas



![índice de caracteres em uma strings](https://cdn.programiz.com/sites/tutorial2program/files/element-slicling.jpg)
