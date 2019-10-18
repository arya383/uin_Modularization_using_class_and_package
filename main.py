program = 'Hukum_Arus'

def Kuat_Arus(tegangan, hambatan):
    Kuat_Arus = tegangan / hambatan
    print(f'Kuat Arus = {Kuat_Arus} Ampere')

Kuat_Arus = Kuat_Arus(10, 5)

def Tegangan(kuat_arus, hambatan):
    Tegangan = kuat_arus * hambatan
    print(f'tegangan = {Tegangan} Volt')

Tegangan = Tegangan(20, 5)

def Hambatan(tegangan, Kuat_arus):
    Hambatan = tegangan / Kuat_arus
    print(f'Hambatan = {Hambatan} Ohm')

Hambatan = Hambatan(50, 5)
