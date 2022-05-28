"<----------------------------- Simulator Astronaut ------------------------------>"
import  random
print("<----------------------------- Simulator Astronaut ------------------------------>")
class Astronaut:
    def __init__(self,name):
        self.name = name
        self.gladness = 50
        self.way = 100             #стільки пролетів від Землі до Марса
        self.oxygen = 100          #вміст кисню на кораблі
        self.health = 100          #здоров'я астронавта
        self.order = 100           #справність корабля
        self.resource = 8500       #ресурс для ремонту корабля
        self.energy = 100          #рівень енергії на кораблі
        self.temperature = 23      #температура на кораблі
        self.power = 100           #потужність двигунів
        self.alive = True
    def crash_oxygen(self):        #витік кисню
        self.oxygen -= 20
        self.gladness -= 1
        self.health -= 7
    def crash_energy(self):        #зменшення енергії
        self.gladness -= 1
        self.energy -= 23
        self.temperature -= 0.1
        self.power -= 10
    def crash_shuttle(self):       #зламався шатл
        self.gladness -= 0.5
        self.way -= 5000
        self.temperature -= 0.3
        self.oxygen -= 12
        self.order -= 10
    def fix_suttle(self):          #ремонт шатла
        self.gladness += 1.5
        self.resource -= 50
        self.energy += 10
        self.order += 12
    def fix_oxygen(self):          #ремонт балона з киснем
        self.oxygen += 10
        self.gladness += 0.5
        self.health += 3
        self.resource -= 15
    def fix_energy(self):          #ремонт енергії
        self.resource -= 30
        self.gladness += 0.5
        self.energy += 23
        self.energy += 1500
        self.power += 10
    def sick(self):                #астронавт захворів
        self.gladness -= 0.05
        self.health -= 10
    def medicine(self):            #лікування астронавта
        self.health += 2
        self.gladness += 1
        self.resource -= 20

    def is_alive(self):
        if self.gladness < 0:                       #перевірка радості
            print("Depresion!")
            self.alive = False
        elif self.way >= 54000000:                  #перевірка перевірка шляху
            print("I reached Mars!")
            self.alive = False
        elif self.oxygen < 5:                       #перевірка кисню
            print("I can smother")
            self.alive = False
        elif self.health <= 10:                     #перевірка здоров'я астронавта
            print("I can die")
        elif self.order <= 0:                       #перевірка справності шатла
            print("My shuttle crushed!Help me!")
            self.alive = False
        elif self.resource <= 0:                    #перевірка кількість ресурсів
            print("I can`t fix my shuttle!")
            self.alive = False
        elif self.energy <= 0:                      #перевірка енергії
            print("Help me!I can`t fly!")
            self.alive = False
        elif self.temperature <= 0:                 #перевірка температури
            print("I can froze!")
            self.alive = False
        elif self.power <= 0:                       #перевірка потужності
            print("I don`t have power to reach Mars")

    def end_of_day(self):
        self.way += 150000
        if self.oxygen > 100:
            self.oxygen = 100
        if self.health > 100:
            self.health = 100
        if self.order > 100:
            self.order = 100
        if self.power > 100:
            self.power = 100
        print(f"Gladness: {round(self.gladness,2)}")
        print(f"Way from Earth: {self.way}км")
        print(f"Oxygen: {self.oxygen}")
        print(f"Health: {self.health}")
        print(f"Order: {self.order}")
        print(f"Resource: {self.resource}")
        print(f"Temperature: {round(self.temperature,2)}")
        print(f"Power: {self.power}")

    def live(self,day):
        day = "Day " + str(day) + "name: " + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1,8)
        if live_cube == 1:
            self.crash_oxygen()
        if live_cube == 2:
            self.crash_energy()
        if live_cube == 3:
            self.crash_shuttle()
        if live_cube == 4:
            self.fix_suttle()
        if live_cube == 5:
            self.fix_oxygen()
        if live_cube == 6:
            self.fix_energy()
        if live_cube == 7:
            self.sick()
        if live_cube == 8:
            self.medicine()
        self.must()
        self.end_of_day()
        self.is_alive()

    def must(self):
        if self.oxygen <= 30:
            self.fix_oxygen()
        if self.energy <= 20:
            self.fix_energy()
        if self.health <= 12:
            self.medicine()
        if self.order <= 30:
            self.fix_suttle()

astronaut = Astronaut("Ostap")
for day in range(366):
    if astronaut.alive == False:
        break
    astronaut.live(day)