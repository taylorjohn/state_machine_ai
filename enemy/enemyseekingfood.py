class EnemyStateSeekingFood(State):
    
    def __init__(self, enemy):
        
        State.__init__(self, "seeking")
        self.enemy = enemy
        self.food_id = None
    
    def check_conditions(self):
        
        food = self.enemy.world.get(self.enemy.food_id)
        if food is None:
            return "exploring"
        
        if self.enemy.location.get_distance_to(food.location) < 5:
        
            self.enemy.carry(food.image)
            self.enemy.world.remove_entity(food)
            return "delivering"
        return None
    
    def entry_actions(self):
    
        food = self.enemy.world.get(self.enemy.food_id)
        if food is not None:                        
            self.enemy.destination = food.location
            self.enemy.speed = 200 + randint(-20, 20)