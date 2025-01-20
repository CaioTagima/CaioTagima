cpf = input("digite seu CPF: ")
cpf_sembarra = cpf.split('-')
cpfnovedig = cpf_sembarra[0]
novedig = cpfnovedig.split('.')
cpfver = int(cpf_sembarra[1][0])
cpfver2 = int(cpf_sembarra[1][1])

#primeiro digito

k = 10
soma = 0 
for numeros in novedig:
    for numero in numeros:
        for num in numero:
            soma += int(num)*k
            k = k-1
primdig = soma * 10 % 11
primdig = primdig if primdig <= 9 else 0
#segundo digito 

dezdig = novedig + list(str(primdig))
n = 11
soma2 = 0 
for numeros in dezdig:
    for numero in numeros:
        for num in numero:
            soma2 += int(num)*n
            n = n-1
segdig = soma2 * 10 % 11
segdig = segdig if segdig <= 9 else 0 

if primdig == cpfver and segdig == cpfver2:
    print("CPF válido")
else:
    print("CPF inválido")




            
            
           
