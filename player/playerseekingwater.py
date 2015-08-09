class PlayerStateSeekingWater(State):
    
    def __init__(self, player):
        
        State.__init__(self, "seeking")
        self.player = player
        self.water_id = None
    
    def check_conditions(self):
        
        water = self.player.world.get(self.player.water_id)
        if water is None:
            return "exploring"
        
        if self.player.location.get_distance_to(water.location) < 5:
        
            self.player.carry(water.image)
            self.player.world.remove_entity(water)
            return "delivering"
        return None
    
    def entry_actions(self):
    
        water = self.player.world.get(self.player.water_id)
        if water is not None:                        
            self.player.destination = water.location
            self.player.speed = 200 + randint(-20, 20)