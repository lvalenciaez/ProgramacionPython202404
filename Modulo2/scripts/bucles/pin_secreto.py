pin_secreto = 'desbloquear'
numero = 0
while numero <= 3 :
    numero+=1
    clave=input('ingrese su clave secreta: ')
    if clave == pin_secreto :
        print('Clave correcta')
        break
    elif numero == 3 :
        print('Celular bloqueado')
        break
    else:
       print('vuelva a digitar su clave')