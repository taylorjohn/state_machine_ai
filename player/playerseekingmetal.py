class PlayerStateSeekingMetal(State):
    
    def __init__(self, player):
        
        State.__init__(self, "seeking")
        self.player = player
        self.metal_id = None
    
    def check_conditions(self):
        
        metal = self.player.world.get(self.player.metal_id)
        if metal is None:
            return "exploring"
        
        if self.player.location.get_distance_to(metal.location) < 5:
        
            self.player.carry(metal.image)
            self.player.world.remove_entity(metal)
            return "delivering"
        return None
    
    def entry_actions(self):
    
        metal = self.player.world.get(self.player.metal_id)
        if metal is not None:                        
            self.player.destination = metal.location
            self.player.speed = 200 + randint(-20, 20)