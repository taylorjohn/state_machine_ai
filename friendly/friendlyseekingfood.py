class FriendlyStateSeekingFood(State):
    
    def __init__(self, friendly):
        
        State.__init__(self, "gathering")
        self.friendly = friendly
        self.food_id = None
    
    def check_conditions(self):
        
        food = self.friendly.world.get(self.friendly.food_id)
        if food is None:
            return "exploring"
        
        if self.friendly.location.get_distance_to(food.location) < 5:
        
            self.friendly.carry(food.image)
            self.friendly.world.remove_entity(food)
            return "delivering"
        return None
    
    def entry_actions(self):
    
        food = self.friendly.world.get(self.friendly.food_id)
        if food is not None:                        
            self.friendly.destination = food.location
            self.friendly.speed = 200 + randint(-20, 20)