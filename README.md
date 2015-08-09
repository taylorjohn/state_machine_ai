# state_machine_ai
08/09/2015 day 1 concept and blocked out files

Create a state machine to control the citzens of town based on random combination of citzen types.

divide map in three, each side is kingdom with random number of villagers. 

The villager are randomly broken down into roles soldiers, cooks, forgers, gathers, runners and builders.

which the simple state machine will control and let time run out till the one town wins.

They go through simple tasks like exploring, seeking, leveling, delivering, fighting, building and cooking

they explore for:

Material
	wood
	rocks
	food

they gather for:

	wood
	rocks
	food

they fight using:

attack
	weapon
		arrow
		swords
		projectile
damage
	troops
	fort
		wood parts
		stone parts
		food storage

They get enrgy from food and water:		
		
cooks
	feed
		citzens

Turn materials into weapong:

forger
	weapons
		crossbow
		swords wood, fire, stone
		catapult
	ammo
		arrow  wood, fire, stone
		projectile wood, fire, stone
		
They build and repair damage to storage and kingdom

builders
	forts
		wood parts
		stone parts
		food storage
		
The run the gathered material from storage area to need areas

runners
	move material from storage to needed areas
		food
		material
		weapons
