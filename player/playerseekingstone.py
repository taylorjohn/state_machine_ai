class PlayerStateSeekingStone(State):
    
    def __init__(self, player):
        
        State.__init__(self, "seeking")
        self.player = player
        self.stone_id = None
    
    def check_conditions(self):
        
        stone = self.player.world.get(self.player.stone_id)
        if stone is None:
            return "exploring"
        
        if self.player.location.get_distance_to(stone.location) < 5:
        
            self.player.carry(stone.image)
            self.player.world.remove_entity(stone)
            return "delivering"
        return None
    
    def entry_actions(self):
    
        stone = self.player.world.get(self.player.stone_id)
        if stone is not None:                        
            self.player.destination = stone.location
            self.player.speed = 200 + randint(-20, 20)