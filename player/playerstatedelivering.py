        
class PlayerStateDelivering(State):
    
    def __init__(self, player):
        
        State.__init__(self, "delivering")
        self.player = player
        
        
    def check_conditions(self):
                
        if Vector2(*BASE_POSITION).get_distance_to(self.player.location) < BASE_SIZE:
            if (randint(1, 10) == 1):
                self.player.drop(self.player.world.background)
                return "exploring"
            
        return None
        
        
    def entry_actions(self):
        
        self.player.speed = 60.        
        random_offset = Vector2(randint(-20, 20), randint(-20, 20))
        self.player.destination = Vector2(*BASE_POSITION) + random_offset     