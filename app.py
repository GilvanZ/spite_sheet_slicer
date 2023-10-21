import pygame
from PIL import Image
pygame.init()



class Button:
    def __init__(self, x, y, width, height, text):
        self.rectangle = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen):
        pygame.draw.rect(screen, (119, 136, 153), self.rectangle)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        screen.blit(text_surface, (self.rectangle.centerx - text_surface.get_width() // 2, self.rectangle.centery - text_surface.get_height() // 2))

width = 800
height = 600
screen = pygame.display.set_mode((width, height))

x, y = 0, 0
height_draw, width_draw = 16, 16
block = False
color_select = (70, 130, 180)

path = input("Path: ")
sprites_sheet = pygame.image.load(path)

font = pygame.freetype.Font(None, 36)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                block = not block
                print("Block =", block)
                color_select = (255, 0, 0) if block else (100, 0, 0)

            if block:
                if event.key == pygame.K_RIGHT:
                    height_draw += 8
                if event.key == pygame.K_LEFT:
                    height_draw = max(8,height_draw  - 8)
                if event.key == pygame.K_UP:
                    width_draw = max(8, width_draw - 8)
                if event.key == pygame.K_DOWN:
                    width_draw += 8
            else:
                if event.key == pygame.K_RIGHT:
                    y += 8
                if event.key == pygame.K_LEFT:
                    y = max(0, y - 8)
                if event.key == pygame.K_DOWN:
                    x += 8
                if event.key == pygame.K_UP:
                    x = max(0, x - 8)
                if event.key == pygame.K_RETURN:    
                    archive_name= input("Archive name: ")
                    sprite = sprites_sheet.subsurface(pygame.Rect(y, x, height_draw, width_draw))
                    sprite_pil = pygame.surfarray.array3d(sprite)
                    sprite_pil = Image.fromarray(sprite_pil)
                    # Save
                    sprite_pil.save(f'sprites_slicer\\saved\\'+archive_name+".png")
                    print(f"Saved on: sprites_slicer/saved/"+archive_name+".png")

    screen.fill((255, 255, 255))
    print(f"x: {x}, y: {y}")




    
    
    screen.blit(sprites_sheet, (0, 0))
    text_surface, _ = font.render("Olá, Pygame!", (255, 255, 255))
    screen.blit(text_surface,(500,500))
    pygame.draw.rect(screen, color_select, (y, x, height_draw, width_draw), 1)

    pygame.display.flip()
    pygame.time.delay(10)
pygame.quit()
