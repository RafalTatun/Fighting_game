import pygame
from support import import_csv_layout, import_cut_graphic
from settings import tile_size
from tiles import Tile, StaticTile

class Level():
    def __init__(self, level_data, surface):
        self.display_surface = surface


        # Player1 setup
        player_layout = import_csv_layout(level_data['player'])
        self.player = pygame.sprite.GroupSingle()
        self.player_setup(player_layout)


        # Terrain setup
        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout, 'terrain')
    
    def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size

                    if type == 'terrain':
                        terrain_tile_list = import_cut_graphic('./assets/images/ground.png')
                        tile_surface = terrain_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)
            

        return sprite_group


    def player_setup(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                
                if val == '0':
                    print('player goes here')
                if val == '1':
                    hat_surface = pygame.image.load('./assets/images/Strawberry/')
                    sprite = StaticTile(tile_size, x, y, surface)

    def run(self):
        # Run the entire level
        self.terrain_sprites.draw(self.display_surface)
        self.terrain_sprites.update()