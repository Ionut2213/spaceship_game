import pygame

# Creating Global Variables

WIDTH = 900
HEIGHT = 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space war ships")
WHITE = (255, 255, 255)








def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.fill(WHITE)
        pygame.display.update()
    pygame.quit()








if __name__ == "__main__":
    main()