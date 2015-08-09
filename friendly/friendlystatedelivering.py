        
class FriendlyStateDelivering(State):
    
    def __init__(self, enemy):
        
        State.__init__(self, "delivering")
        self.friendly = friendly
        
        
    def check_conditions(self):
                
        if Vector2(*BASE_POSITION).get_distance_to(self.friendly.location) < BASE_SIZE:
            if (randint(1, 10) == 1):
                self.friendly.drop(self.friendly.world.background)
                return "exploring"
            
        return None
        
        
    def entry_actions(self):
        
        self.friendly.speed = 60.        
        random_offset = Vector2(randint(-20, 20), randint(-20, 20))
        self.friendly.destination = Vector2(*BASE_POSITION) + random_offset     