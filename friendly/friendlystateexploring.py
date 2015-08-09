class FriendlyStateExploring(State):
    
    def __init__(self, friendly):
        
        State.__init__(self, "exploring")
        self.friendly = friendly
        
    def random_destination(self):
        
        w, h = SCREEN_SIZE
        self.friendly.destination = Vector2(randint(0, w), randint(0, h))    
    
    def do_actions(self):
        
        if randint(1, 20) == 1:
            self.random_destination()
            
    def check_conditions(self):
                        
        water = self.friendly.world.get_close_entity("water", self.friendly.location)        
        if water is not None:
            self.friendly.water_id = water.id
            return "seekingwater" 

        wood = self.friendly.world.get_close_entity("wood", self.friendly.location)        
        if wood is not None:
            self.friendly.wood_id = wood.id
            return "seekingwood"

        stone = self.friendly.world.get_close_entity("stone", self.friendly.location)        
        if stone is not None:
            self.friendly.stone_id = stone.id
            return "seekingstone"

        metal = self.friendly.world.get_close_entity("metal", self.friendly.location)        
        if metal is not None:
            self.friendly.metal_id = metal.id
            return "seekingmetal"

        food = food.friendly.world.get_close_entity("food", self.friendly.location)        
        if metal is not None:
            food.friendly.metal_id = food.id
            return "seekingfood"     
                
        soldier = self.friendly.world.get_close_entity("soldier", BASE_POSITION, BASE_SIZE)        
        if soldier is not None:
            if self.friendly.location.get_distance_to(soldier.location) < 100:
                self.friendly.soldier_id = soldier.id
                return "fighting"
        
        return None
    
    def entry_actions(self):
        
        self.friendly.speed = 120. + randint(-30, 30)
        self.random_destination()