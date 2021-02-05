import random as rd
"""
cw dec_bin
cw dec_exa
cw potegi_2
cw rejestry
cw flagi
"""

class cwiczenia:
    @staticmethod
    def STARTCW_dec_bin():
        x=True
        print("|--------------------BIN-----------------------------|")
        while x:
            n=rd.randint(0,16)
            print(f'The number is {n}')
            nn=str(input('The number in binary is: '))
            if nn==bin(n)[2:]:
                print("Good! ")
            else:
                print("Error! ")
                x=False
                c.dec_exa()
        
    @staticmethod
    def dec_exa():
        x=True
        print("|------CHANGED---------HEX----------------------------|")
        while x:
            n=rd.randint(10,15)
            print(f'The number is: {n}')
            nn=str(input('The number in hex is: '))
            if nn.upper()==hex(n)[2:].upper():
                print("Good! ")
            else:
                print("Error! ")
                x=False
                c.potegi_2()
        
    @staticmethod
    def potegi_2():
        x=True
        print("|------CHANGED---------P^2----------------------------|")
        while x:
            n=rd.randint(0,16)
            print(f'The number is: 2^{n}')
            nn=str(input('The number is: '))
            if nn == str(2**n):
                print("Good! ")
            else:
                print("Error! ")
                x=False
                c.rejestry()
        
    @staticmethod
    def rejestry():
        x=True
        print("|------CHANGED---------REG----------------------------|")
        dict={
            "Akumulatora":"AX",
            "Rejestru bazowego":"BX",
            "Rejestru zliczajcego":"CX",
            "Rejestru danych":"DX",
            "Wskaznikastosu":"SP",
            "Wskaznika bazy":"BP",
            "Indeksu zrodlowego":"SI",
            "Indeksu docelowego":"DI",
            "Segmentu kodu":"CS",
            "Segmentu danych":"DS",
            "Segmentu stosu":"SS",
            "Segmentu dodatkowego":"ES",
            "Wskaznika rozkazow":"IP"
            }
        while x:
            key=rd.choice(list(dict))
            print(f'Podac skrot {key}: ')
            answer=str(input("Skrot jest: "))
            if answer.upper()==dict[key]:
                print("Good! ")
            else:
                print("Error! ")
                x=False
                c.flagi()
    @staticmethod
    def flagi():
        x=True
        print("|------CHANGED--------FLAGS---------------------------|")
        dict={
            "na skutek dzialania nastapilo przeniesienie z MSB na zewnatrz":"CF",
            "w wyniku dzialania liczba bitow w LSB jest parzysta":"PF",
            "nastepuje przeniesienie bit(3,4) lub pozyczka bit(4,3)":"AF",
            "w wyniku dzialania wynik jest zero":"ZF",
            "w wyniku dzialania MSB jest 1":"SF",
            "wartosc jest 1 gdy po kazdej instrukcji jest wywolane przerwanie pracy krkowej":"TF",
            "wartosc jest 1 ,to przerwanie sprzetowe ma byc wykonane natychmiast":"IF",
            ", jak wartosc wynosi 1, to dane sa pobierane w kierunku malejacym adresu pamieci":"DF",
            "jak wystepuje przypelnienie,wartosc wynosi 1":"OF"
            }
        while x:
            key=rd.choice(list(dict))
            print(f'Podac skrot flagi w ktorej {key}')
            answer=str(input("Skrot jest: "))
            if answer.upper()==dict[key]:
                print("Good! ")
            else:
                print("Error! ")
                x=False
                break
        
c=cwiczenia()
c.STARTCW_dec_bin()