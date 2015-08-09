        
class EnemyStateDelivering(State):
    
    def __init__(self, enemy):
        
        State.__init__(self, "delivering")
        self.enemy = enemy
        
        
    def check_conditions(self):
                
        if Vector2(*BASE_POSITION).get_distance_to(self.enemy.location) < BASE_SIZE:
            if (randint(1, 10) == 1):
                self.enemy.drop(self.enemy.world.background)
                return "exploring"
            
        return None
        
        
    def entry_actions(self):
        
        self.enemy.speed = 60.        
        random_offset = Vector2(randint(-20, 20), randint(-20, 20))
        self.enemy.destination = Vector2(*BASE_POSITION) + random_offset     