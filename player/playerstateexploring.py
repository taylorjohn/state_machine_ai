class PlayerStateExploring(State):
    
    def __init__(self, player):
        
        State.__init__(self, "exploring")
        self.player = player
        
    def random_destination(self):
        
        w, h = SCREEN_SIZE
        self.player.destination = Vector2(randint(0, w), randint(0, h))    
    
    def do_actions(self):
        
        if randint(1, 20) == 1:
            self.random_destination()
            
    def check_conditions(self):
                        
        water = self.player.world.get_close_entity("water", self.player.location)        
        if water is not None:
            self.player.water_id = water.id
            return "seekingwater" 

        wood = self.player.world.get_close_entity("wood", self.player.location)        
        if wood is not None:
            self.player.wood_id = wood.id
            return "seekingwood"

        stone = self.player.world.get_close_entity("stone", self.player.location)        
        if stone is not None:
            self.player.stone_id = stone.id
            return "seekingstone"

        metal = self.player.world.get_close_entity("metal", self.player.location)        
        if metal is not None:
            self.player.metal_id = metal.id
            return "seekingmetal"

        food = food.player.world.get_close_entity("food", self.player.location)        
        if food is not None:
            self.player.food_id = food.id
            return "seekingfood"     
                
        soldier = self.player.world.get_close_entity("soldier", BASE_POSITION, BASE_SIZE)        
        if soldier is not None:
            if self.player.location.get_distance_to(soldier.location) < 100:
                self.player.soldier_id = soldier.id
                return "fighting"
        
        return None
    
    def entry_actions(self):
        
        self.player.speed = 120. + randint(-30, 30)
        self.random_destination()