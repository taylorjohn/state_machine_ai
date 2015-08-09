class FriendlyStateSeekingMetal(State):
    
    def __init__(self, friendly):
        
        State.__init__(self, "seeking")
        self.friendly = friendly
        self.metal_id = None
    
    def check_conditions(self):
        
        metal = self.friendly.world.get(self.friendly.metal_id)
        if metal is None:
            return "exploring"
        
        if self.friendly.location.get_distance_to(metal.location) < 5:
        
            self.friendly.carry(metal.image)
            self.friendly.world.remove_entity(metal)
            return "delivering"
        return None
    
    def entry_actions(self):
    
        metal = self.friendly.world.get(self.friendly.metal_id)
        if metal is not None:                        
            self.friendly.destination = metal.location
            self.friendly.speed = 200 + randint(-20, 20)