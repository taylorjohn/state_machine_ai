class FriendlyStateSeekingStone(State):
    
    def __init__(self, friendly):
        
        State.__init__(self, "seeking")
        self.friendly = friendly
        self.stone_id = None
    
    def check_conditions(self):
        
        stone = self.friendly.world.get(self.friendly.stone_id)
        if stone is None:
            return "exploring"
        
        if self.friendly.location.get_distance_to(stone.location) < 5:
        
            self.friendly.carry(stone.image)
            self.friendly.world.remove_entity(stone)
            return "delivering"
        return None
    
    def entry_actions(self):
    
        stone = self.friendly.world.get(self.friendly.stone_id)
        if stone is not None:                        
            self.friendly.destination = stone.location
            self.friendly.speed = 200 + randint(-20, 20)