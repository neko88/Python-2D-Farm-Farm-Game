from os import walk
import pygame



def import_folder(path):
    ## Store all surfaces
    surface_list = []

    #folder name, sub folder, file
    for _, _, img_files in walk(path):
        for image_name in img_files:
            full_path = path + '/' + image_name
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list