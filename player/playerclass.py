class Player(GameEntity):
    
    def __init__(self, world, image):
        
        GameEntity.__init__(self, world, "player", image)
        
        exploring_state = PlayerStateExploring(self)
        seeking_state = PlayerStateSeeking(self)
        leveling_state = PlayerStateLeveling(self)
        delivering_state = PlayerStateDelivering(self)
        hunting_state = PlayerStateHunting(self)
        
        self.brain.add_state(exploring_state)
        self.brain.add_state(seeking_state)
        self.brain.add_state(leveling_state)
        self.brain.add_state(delivering_state)
        self.brain.add_state(hunting_state)
        
        self.carry_image = None
        
    def carry(self, image):
        
        self.carry_image = image
        
    def drop(self, surface):
        
        if self.carry_image:
            x, y = self.location
            w, h = self.carry_image.get_size()
            surface.blit(self.carry_image, (x-w, y-h/2))
            self.carry_image = None
        
    def render(self, surface):
        
        GameEntity.render(self, surface)
        
        if self.carry_image:
            x, y = self.location
            w, h = self.carry_image.get_size()
            surface.blit(self.carry_image, (x-w, y-h/2))