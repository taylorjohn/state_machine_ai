class FriendlyStateSeekingWater(State):
    
    def __init__(self, friendly):
        
        State.__init__(self, "seeking")
        self.friendly = friendly
        self.water_id = None
    
    def check_conditions(self):
        
        water = self.friendly.world.get(self.friendly.water_id)
        if water is None:
            return "exploring"
        
        if self.friendly.location.get_distance_to(water.location) < 5:
        
            self.friendly.carry(water.image)
            self.friendly.world.remove_entity(water)
            return "delivering"
        return None
    
    def entry_actions(self):
    
        water = self.friendly.world.get(self.friendly.water_id)
        if water is not None:                        
            self.friendly.destination = water.location
            self.friendly.speed = 200 + randint(-20, 20)