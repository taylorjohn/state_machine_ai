class EnemyStateSeekingMetal(State):
    
    def __init__(self, enemy):
        
        State.__init__(self, "seeking")
        self.enemy = enemy
        self.metal_id = None
    
    def check_conditions(self):
        
        metal = self.enemy.world.get(self.enemy.metal_id)
        if metal is None:
            return "exploring"
        
        if self.enemy.location.get_distance_to(metal.location) < 5:
        
            self.enemy.carry(metal.image)
            self.enemy.world.remove_entity(metal)
            return "delivering"
        return None
    
    def entry_actions(self):
    
        metal = self.enemy.world.get(self.enemy.metal_id)
        if metal is not None:                        
            self.enemy.destination = metal.location
            self.enemy.speed = 200 + randint(-20, 20)