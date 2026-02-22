def repetir_cero(*args):
    for item in range(len(args)-1):

        if args[item] == args[item+1]:
            if args[item] == 0:
                return True

    return False

print(repetir_cero(5,6,1,0,0,9,3,5))
print(repetir_cero(6,0,5,1,0,3,0,1))
print(repetir_cero(0,0,5,1,1,3,1,1))
print(repetir_cero(0,1,5,1,1,3,1,1))