import pygame

pygame.init()


WIDTH, HEIGHT = 500, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clicker Game")

font = pygame.font.SysFont(None, 36)


score = 0
click_power = 1
auto_income = 0

upgrade_cost = 50
auto_upgrade_cost = 100


click_button = pygame.Rect(150, 200, 200, 100)
upgrade_button = pygame.Rect(150, 330, 200, 70)
auto_button = pygame.Rect(150, 420, 200, 70)

clock = pygame.time.Clock()


AUTO_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(AUTO_EVENT, 1000)


def draw():
    screen.fill((30, 30, 30))


    pygame.draw.rect(screen, (0, 200, 0), click_button)
    screen.blit(font.render("CLICK", True, (255, 255, 255)), (200, 235))

    pygame.draw.rect(screen, (0, 100, 200), upgrade_button)
    screen.blit(font.render(f"+Click ({upgrade_cost})", True, (255, 255, 255)), (140, 350))

    pygame.draw.rect(screen, (200, 100, 0), auto_button)
    screen.blit(font.render(f"Auto ({auto_upgrade_cost})", True, (255, 255, 255)), (150, 440))


    screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (150, 50))
    screen.blit(font.render(f"Power: {click_power}", True, (255, 255, 0)), (150, 90))
    screen.blit(font.render(f"Auto: {auto_income}/sec", True, (0, 255, 255)), (140, 130))
    screen.blit(font.render("Goal: 1,000,000", True, (255, 215, 0)), (140, 170))

    if score >= 1_000_000:
        screen.blit(font.render("YOU WIN!", True, (255, 215, 0)), (170, 580))

    pygame.display.flip()


running = True
while running:
    clock.tick(60)


    events = pygame.event.get()
    for event in events:

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            if click_button.collidepoint(mouse_pos):
                score += click_power

            elif upgrade_button.collidepoint(mouse_pos):
                if score >= upgrade_cost:
                    score -= upgrade_cost
                    click_power += 1
                    upgrade_cost = int(upgrade_cost * 1.5)

            elif auto_button.collidepoint(mouse_pos):
                if score >= auto_upgrade_cost:
                    score -= auto_upgrade_cost
                    auto_income += 1
                    auto_upgrade_cost = int(auto_upgrade_cost * 1.7)

        elif event.type == AUTO_EVENT:
            score += auto_income

    draw()

pygame.quit()