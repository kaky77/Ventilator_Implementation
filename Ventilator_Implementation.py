

class Ventilator:

    # ventilator constructor with 4 parameters
    def __init__(self, color, speed, direction):
        self.color = color              # color is the string 
        self.speed = speed              # speed is the number between [0, 3]
                                        # 0 -> imply off (speed = 0)
                                        # 1 -> imply speed = 1 
                                        # 2 -> imply speed = 2 
                                        # 3 -> imply speed = 3 
        self.direction = direction      # direction is the number between 1 and -1 
                                        # 1 -> imply clockwise
                                        # -1 -> imply reverse 
        pass

    # method firs_cord who permit to increase ventilator speed
    def first_Cord(self, speed):
        self.speed = speed 
        pass

    # method Second_Cord who permit to reverse the direction of the ventilator while maintaining its speed 
    def Second_Cord(self, direction):
        self.direction = direction 
        pass

    # method Setting_Ventilator for to display Ventilator 
    def Setting_Ventilator(self):
        print("__ Ventilator __")
        print()
        print("color      -> " + self.color)
        print("speed      ->", self.speed)
        print("direction  ->", self.direction )
        pass

    pass



# --- MAIN ---

Ventilateur1 = Ventilator("black",2,1)
Ventilateur1.Setting_Ventilator()
Ventilateur1.first_Cord(3)
print()
Ventilateur1.Setting_Ventilator()
Ventilateur1.Second_Cord(-1)
Ventilateur1.first_Cord(0)
print()
Ventilateur1.Setting_Ventilator()