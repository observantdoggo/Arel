import tcod as libtcod
from random import randint

from components.equipment import Equipment
from components.equippable import Equippable
from components.item import Item
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level

from condition_functions import Poison, Healing

from entity import Entity

from equipment_slots import EquipmentSlots

from game_messages import MessageLog

from game_states import GameStates

from map_objects.game_map import GameMap

from render_functions import RenderOrder

def load_customfont():
    #The index of the first custom tile in the file
    a = 256
 
    for y in range(5,20):
        libtcod.console_map_ascii_codes_to_font(a, 32, 0, y)
        a += 32


def get_constants():

    load_customfont()

    window_title = "A'Rel"

    screen_width = 60
    screen_height = 40

    bar_width = 20
    panel_height = 7
    panel_y = screen_height - panel_height

    message_x = bar_width + 2
    message_width = screen_width - bar_width - 2
    message_height = panel_height - 1

    map_width = 60
    map_height = 33

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    fov_algorithm = 0
    fov_light_walls = True
    fov_radius = 10

    max_monsters_per_room = 3
    max_items_per_room = 200
    
    options_difficulty = "Standard"
    options_enemy_damage_scale = 100
    options_player_damage_scale = 100
    options_xp_multiplier = 1
    options_luck_scale = 100
    options_death_delete_save = True
    options_tutorial_enabled = True

    colors = {
        'dark_wall': libtcod.Color(34, 34, 68),
        'dark_ground': libtcod.Color(17, 17, 34),
        'light_wall': libtcod.Color(102, 102, 153),
        'light_ground': libtcod.Color(34, 34, 68)
    }

    constants = {
        'window_title': window_title,
        'screen_width': screen_width,
        'screen_height': screen_height,
        'bar_width': bar_width,
        'panel_height': panel_height,
        'panel_y': panel_y,
        'message_x': message_x,
        'message_width': message_width,
        'message_height': message_height,
        'map_width': map_width,
        'map_height': map_height,
        'room_max_size': room_max_size,
        'room_min_size': room_min_size,
        'max_rooms': max_rooms,
        'fov_algorithm': fov_algorithm,
        'fov_light_walls': fov_light_walls,
        'fov_radius': fov_radius,
        'max_monsters_per_room': max_monsters_per_room,
        'max_items_per_room': max_items_per_room,
        'colors': colors,
        'options_difficulty': options_difficulty,
        'options_enemy_damage_scale': options_enemy_damage_scale,
        'options_player_damage_scale': options_player_damage_scale,
        'options_xp_multiplier': options_xp_multiplier,
        'options_luck_scale': options_luck_scale,
        'options_death_delete_save': options_death_delete_save,
        'options_tutorial_enabled': options_tutorial_enabled
    }

    return constants
    
    #random.choice[colors_list['Scrolls']]
    
def get_render_colors():
    colors_list = {
    'Scrolls':                      [
                                    libtcod.Color(255, 236, 158),
                                    libtcod.Color(255, 221, 138),
                                    libtcod.Color(225, 173, 109),
                                    libtcod.Color(201, 145, 87),
                                    libtcod.Color(210, 170, 119)
                                    ],
    'White Potion':                 libtcod.Color(255, 255, 255),
    'Yellow Potion':                libtcod.Color(255, 255, 0),
    'Blue Potion':                  libtcod.Color(0, 0, 255),
    'Red Potion':                   libtcod.Color(255, 0, 0),
    'Green Potion':                 libtcod.Color(0, 255, 0),
    'Black Potion':                 libtcod.Color(50, 50, 50),
    'Brown Potion':                 libtcod.Color(145, 63, 0),
    'Azure Potion':                 libtcod.Color(0, 50, 100),
    'Ivory Potion':                 libtcod.Color(100, 100, 94),
    'Teal Potion':                  libtcod.Color(0, 50, 50),
    'Silver Potion':                libtcod.Color(175, 175, 175),
    'Purple Potion':                libtcod.Color(150, 0, 150),
    'Gray Potion':                  libtcod.Color(100, 100, 100),
    'Orange Potion':                libtcod.Color(100, 65, 0),
    'Maroon Potion':                libtcod.Color(50, 0, 0),
    'Charcoal Potion':              libtcod.Color(80, 80, 80),
    'Aquamarine Potion':            libtcod.Color(50, 100, 83),
    'Coral Potion':                 libtcod.Color(100, 50, 31),
    'Fuchsia Potion':               libtcod.Color(200, 0, 200),
    'Crimson Potion':               libtcod.Color(83, 8, 24),
    'Khaki Potion':                 libtcod.Color(94, 90, 55),
    'Magenta Potion':               libtcod.Color(100, 20, 100),
    'Golden Potion':                libtcod.Color(212, 175, 55),
    'Plum Potion':                  libtcod.Color(87, 63, 87),
    'Olive Potion':                 libtcod.Color(50, 50, 0),
    'Cyan Potion':                  libtcod.Color(0, 100, 100)
    }
    
    return colors_list
    
def get_unidentified_names():
    
    potion_colors_list = [    
    'White',
    'Yellow',
    'Blue',
    'Red',
    'Green',
    'Black',
    'Brown',
    'Azure',
    'Ivory',
    'Teal',
    'Silver',
    'Purple',
    'Gray',
    'Orange',
    'Maroon',
    'Charcoal',
    'Aquamarine',
    'Coral',
    'Fuchsia',
    'Crimson',
    'Khaki',
    'Magenta',
    'Golden',
    'Plum',
    'Olive',
    'Cyan'
    ]
    
    scroll_names_list = [
    "FOO",
    "UBAR",
    "NR 9",
    "JAPE",
    "ODOG",
    "FREY",
    "MACK",
    "RBDKY", 
    "DNGD",
    "NTHK",
    "YREJ",
    "ETAN",
    "KIAL",
    "REBE"
    ]
    
    names_list = {
    'Player':               "Player",
    'Goblin':               "Goblin",
    'Troll':                "Troll",
    'Camera Op.':           "Camera Op.",
    'Dagger':               "Dagger",
    'Sword':                "Sword",
    'Shield':               "Shield",
    'Healing Potion':       (str(get_item(potion_colors_list)) + " Potion"),
    'Lightning Scroll':     ("Scroll labeled '" + str(get_item(scroll_names_list)) + "'"),
    'Fireball Scroll':      ("Scroll labeled '" + str(get_item(scroll_names_list)) + "'"),
    'Confusion Scroll':     ("Scroll labeled '" + str(get_item(scroll_names_list)) + "'")
    
    }
    
    return names_list
    
def get_item(item_list, index=0):
    #return a random item from a list, and remove that item from the list.
    
    if len(item_list) == 0: return "oops"
    
    i = randint(0, len(item_list)-1)
    item = item_list[i]
    item_list.remove(item_list[i])
    
    return item
    

def get_game_variables(constants, names_list, render_colors_list):
    fighter_component = Fighter(hp=100, defense=1, power=2, speed=5)
    inventory_component = Inventory(50)
    level_component = Level()
    equipment_component = Equipment()
    player = Entity(0, 0, 256, libtcod.white, 'Player', blocks=True, render_order=RenderOrder.ACTOR,
                    fighter=fighter_component, inventory=inventory_component, level=level_component,
                    equipment=equipment_component)
    player.conditions.append(Poison(target=player, active=True, duration=8, damage=2))
    player.conditions.append(Healing(target=player, active=True, duration=10, healing=1))
    entities = [player]

    item_component = Item(description="A short rusty dagger. It's dull and has notches missing from the blade.")
    equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=2)
    dagger = Entity(0, 0, 368, libtcod.sky, 'Dagger', equippable=equippable_component, item=item_component)
    player.inventory.add_item(dagger, names_list)
    player.equipment.toggle_equip(dagger)

    game_map = GameMap(constants['map_width'], constants['map_height'])
    game_map.make_map(constants['max_rooms'], constants['room_min_size'], constants['room_max_size'],
                      constants['map_width'], constants['map_height'], player, entities, names_list, render_colors_list)
   

    
    message_log = MessageLog(constants['message_x'], constants['message_width'], constants['message_height'])

    game_state = GameStates.PLAYERS_TURN

    return player, entities, game_map, message_log, game_state
