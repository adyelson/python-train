idade = int(input("Insira idade: "))
peso = int(input("Insira peso: "))
horasSono = int(input("Insira horas de sono nas ultimas 24h: "))

if(idade>16 and idade<65):
    if(peso>50):
        if(horasSono>=6):
            print("Você pode doar Sangue")
        else:
            print("Você deve dormir pelo menos 6h.")
    else:
        print("Você deve pesar mais que 50kg")
else:
    print("Você deve ter entre 16 e 65 anos de idade")