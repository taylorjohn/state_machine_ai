class FriendlyStateSeekingWood(State):
    
    def __init__(self, friendly):
        
        State.__init__(self, "seeking")
        self.friendly = friendly
        self.wood_id = None
    
    def check_conditions(self):
        
        wood = self.friendly.world.get(self.friendly.wood_id)
        if wood is None:
            return "exploring"
        
        if self.friendly.location.get_distance_to(wood.location) < 5:
        
            self.friendly.carry(wood.image)
            self.friendly.world.remove_entity(wood)
            return "delivering"
        return None
    
    def entry_actions(self):
    
        wood = self.friendly.world.get(self.friendly.wood_id)
        if wood is not None:                        
            self.friendly.destination = wood.location
            self.friendly.speed = 200 + randint(-20, 20)