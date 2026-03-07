class car:
    wheels=4
    engine="Petrol"
    Top_Speed="120kmph"
    gears=5

    def __init__(self,air_bags,wheels,engine,Top_speed,gears):

        self.air_bags=air_bags
        self.wheels=wheels
        self.engine=engine
        self.Top_Speed=Top_speed
        self.gears=gears
     
     #object metthods
    def display_properties(self):
        d={"wheels":self.wheels,
           "airbags":self.air_bags}
        print(d)
    #object Methods
    def update_base_speed(self,new_speed):
        self.Top_Speed=new_speed
        print(f"Top_speed of car is:{self.Top_Speed}")   

    #class Methods
    @classmethod
    def update_gears(cls,gears):
        cls.gears=gears
        print(f"now gears of  all class objcts will be {cls.gears} ")         



Tata=car(True,4,"Hybrid","140Kmph",6)
Tata.update_base_speed("180kmph")
Tata.display_properties()
car.update_gears(8)
# suzuki=car()
# suzuki.engine="diesal"
# suzuki.gears=4
# suzuki.Top_Speed="110kmph"


# Tata=car()
# # print(Tata.gears)
# Tata.air_bags=True
