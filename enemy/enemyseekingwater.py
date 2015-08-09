class EnemyStateSeekingWater(State):
    
    def __init__(self, enemy):
        
        State.__init__(self, "seeking")
        self.enemy = enemy
        self.water_id = None
    
    def check_conditions(self):
        
        water = self.enemy.world.get(self.enemy.water_id)
        if water is None:
            return "exploring"
        
        if self.enemy.location.get_distance_to(water.location) < 5:
        
            self.enemy.carry(water.image)
            self.enemy.world.remove_entity(water)
            return "delivering"
        return None
    
    def entry_actions(self):
    
        water = self.enemy.world.get(self.enemy.water_id)
        if water is not None:                        
            self.enemy.destination = water.location
            self.enemy.speed = 200 + randint(-20, 20)