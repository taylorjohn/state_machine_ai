class PlayerStateSeekingWood(State):
    
    def __init__(self, player):
        
        State.__init__(self, "seeking")
        self.player = player
        self.wood_id = None
    
    def check_conditions(self):
        
        wood = self.player.world.get(self.player.wood_id)
        if wood is None:
            return "exploring"
        
        if self.player.location.get_distance_to(wood.location) < 5:
        
            self.player.carry(wood.image)
            self.player.world.remove_entity(wood)
            return "delivering"
        return None
    
    def entry_actions(self):
    
        wood = self.player.world.get(self.player.wood_id)
        if wood is not None:                        
            self.player.destination = wood.location
            self.player.speed = 200 + randint(-20, 20)