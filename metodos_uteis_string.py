#alguns metodos em python, mudando alguns caracteres e modificando o texto.
curso = "pYtHOn"

print(curso.upper())
#vai deixar o texto maiusculo

print(curso.lower())
#vai deixar o texto minusculo

print(curso.title())
#vai deixar a primeira letra maiuscula



texto = " corinthians  "

print(texto)

print(texto.strip())
#o strip vai tirar todos os espacos em branco.

print(texto.rstrip())
#o rstrip vai tirar todos os espacos em branco do lado direito, ou seja, vai continuar os espacos do lado esquerdo

print(texto.lstrip())
#o rstrip vai tirar todos os espacos em branco do lado esquero, ou seja, vai continuar os espacos do lado direito



menu = "Darlan"

print("####"+menu+"####")


print(menu.center(14))
#aqui eu passei o espaco que eu quero que esteja. ou seja, a palavra vai ficar centralizado e do lado vai ficar espacos em brancos da quantitade de caracteres que eu colocar. nesse coloquei 14.

print(menu.center(14, "#"))
#aqui é a mesma coisa, coloquei a quantidade de caracterer, e quando eu passsei a virgula eu coloquei o que eu quero que fique no lugar do espaco, se eu nao quiser uns espacos em branco eu escolho algo para colocar.



print("-".join(menu))
#isso serve para colocar algo no meio na palavre, nesse exemplo a palavra vai ficar p-y-t-h-o-n.