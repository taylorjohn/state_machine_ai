class PlayerStateSeekingFood(State):
    
    def __init__(self, player):
        
        State.__init__(self, "seeking")
        self.player = player
        self.food_id = None
    
    def check_conditions(self):
        
        food = self.player.world.get(self.player.food_id)
        if food is None:
            return "exploring"
        
        if self.player.location.get_distance_to(food.location) < 5:
        
            self.player.carry(food.image)
            self.player.world.remove_entity(food)
            return "delivering"
        return None
    
    def entry_actions(self):
    
        food = self.player.world.get(self.player.food_id)
        if food is not None:                        
            self.player.destination = food.location
            self.player.speed = 200 + randint(-20, 20)