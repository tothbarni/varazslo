from Jatekos import Jatekos

class Jatekter:
    def __intit__(self):
        self.harcos=Jatekos("Lakatos Leopold",0,"támogató","🐵")
        self.varazslo=Jatekos("Varázsló",2,"varázsló","👾")
        self.lista = ["_", "_", "_"]
        self.lista[self.harcos.poz] = self.harcos.emo
        self.lista[self.varazslo.poz] = self.varazslo.emo
        self.kor=1
        self.kiir()

    def kiir(self):
        print(f"{self.kor}. kör")
        print("*"*17,"  ","-"*34,"      ","-"*27,"  ")
        print(f"* {self.lista[0]:<3} {self.lista[1]:^3} {self.lista[2]:>3} *    | A {self.harcos.nev} életereje: {self.harcos.hp} |        | A {self.varazslo.nev} életereje: {self.varazslo.hp} |")
        print("*"*17,"  ","-"*34,"      ","-"*27,"  ")
        print("")

    def jatekmenet(self):
        while ((self.harcos.hp > 0) and (self.varazslo.hp > 0)):
            self.harcos.set_pozicio()
            self.varazslo.set_pozicio()
            self.lista = ["_", "_", "_"]
            self.lista[self.harcos.poz] = self.harcos.emo
            self.lista[self.varazslo.poz] = self.varazslo.emo
            if (self.harcos.poz == self.varazslo.poz):
                self.lista[self.varazslo.poz]="⚔️"
                # Itt harcolnak
                self.harcos.set_hp()
                self.varazslo.set_hp()
            self.kor += 1
            self.kiir()
            input()