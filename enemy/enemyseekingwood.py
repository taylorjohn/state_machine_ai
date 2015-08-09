class EnemyStateSeekingWood(State):
    
    def __init__(self, enemy):
        
        State.__init__(self, "seeking")
        self.enemy = enemy
        self.wood_id = None
    
    def check_conditions(self):
        
        wood = self.enemy.world.get(self.enemy.wood_id)
        if wood is None:
            return "exploring"
        
        if self.enemy.location.get_distance_to(wood.location) < 5:
        
            self.enemy.carry(wood.image)
            self.enemy.world.remove_entity(wood)
            return "delivering"
        return None
    
    def entry_actions(self):
    
        wood = self.enemy.world.get(self.enemy.wood_id)
        if wood is not None:                        
            self.enemy.destination = wood.location
            self.enemy.speed = 200 + randint(-20, 20)