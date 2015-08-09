class EnemyStateSeekingStone(State):
    
    def __init__(self, enemy):
        
        State.__init__(self, "seeking")
        self.enemy = enemy
        self.stone_id = None
    
    def check_conditions(self):
        
        stone = self.enemy.world.get(self.enemy.stone_id)
        if stone is None:
            return "exploring"
        
        if self.enemy.location.get_distance_to(stone.location) < 5:
        
            self.enemy.carry(stone.image)
            self.enemy.world.remove_entity(stone)
            return "delivering"
        return None
    
    def entry_actions(self):
    
        stone = self.enemy.world.get(self.enemy.stone_id)
        if stone is not None:                        
            self.enemy.destination = stone.location
            self.enemy.speed = 200 + randint(-20, 20)