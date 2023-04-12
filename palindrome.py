def palindrome(palabra):
    palabra=palabra.lower()#palabra en minuscula
    palabra=palabra.replace(" ","")#elimina espacios
    palabraAlReves=""
    for i in range(len(palabra)-1,-1,-1) :
        palabraAlReves=palabraAlReves+palabra[i] 
    if palabra == palabraAlReves:
        return True 
    else: return False   

    


