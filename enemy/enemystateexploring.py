class EnemyStateExploring(State):
    
    def __init__(self, enemy):
        
        State.__init__(self, "exploring")
        self.enemy = enemy
        
    def random_destination(self):
        
        w, h = SCREEN_SIZE
        self.enemy.destination = Vector2(randint(0, w), randint(0, h))    
    
    def do_actions(self):
        
        if randint(1, 20) == 1:
            self.random_destination()
            
    def check_conditions(self):
                        
        water = self.enemy.world.get_close_entity("water", self.enemy.location)        
        if water is not None:
            self.enemy.water_id = water.id
            return "seekingwater" 

        wood = self.enemy.world.get_close_entity("wood", self.enemy.location)        
        if wood is not None:
            self.enemy.wood_id = wood.id
            return "seekingwood"

        stone = self.enemy.world.get_close_entity("stone", self.enemy.location)        
        if stone is not None:
            self.enemy.stone_id = stone.id
            return "seekingstone"

        metal = self.enemy.world.get_close_entity("metal", self.enemy.location)        
        if metal is not None:
            self.enemy.metal_id = metal.id
            return "seekingmetal"

        food = food.enemy.world.get_close_entity("food", self.enemy.location)        
        if metal is not None:
            food.enemy.metal_id = food.id
            return "seekingfood"     
                
        soldier = self.enemy.world.get_close_entity("soldier", BASE_POSITION, BASE_SIZE)        
        if soldier is not None:
            if self.enemy.location.get_distance_to(soldier.location) < 100:
                self.enemy.soldier_id = soldier.id
                return "fighting"
        
        return None
    
    def entry_actions(self):
        
        self.enemy.speed = 120. + randint(-30, 30)
        self.random_destination()