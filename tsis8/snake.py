import random

import pygame

pygame.init()
WIDTH, HEIGHT = 800, 800
BLACK = (0, 0, 0)
GRID = (69, 123, 0)
RED = (255, 0, 0)
BODY = (6, 79, 0)
YELLOW = (255, 255, 0)
GRASS = (69, 163, 0)

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
BLOCK_SIZE = 40

pygame.display.set_caption('Snake v2.0')
score_font = pygame.font.SysFont("Verdana", 20)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Food:
    def __init__(self, x, y):
        self.location = Point(x, y)

    @property
    def x(self):
        return self.location.x

    @property
    def y(self):
        return self.location.y

    def update(self):
        pygame.draw.rect(
            SCREEN,
            RED,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )


class Snake:
    def __init__(self):
        self.points = [
            Point(WIDTH // BLOCK_SIZE // 2, HEIGHT // BLOCK_SIZE // 2),
            Point(WIDTH // BLOCK_SIZE // 2 + 1, HEIGHT // BLOCK_SIZE // 2),
        ]

    def update(self):
        head = self.points[0]

        pygame.draw.rect(
            SCREEN,
            YELLOW,
            pygame.Rect(
                head.x * BLOCK_SIZE,
                head.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
        for body in self.points[1:]:
            pygame.draw.rect(
                SCREEN,
                BODY,
                pygame.Rect(
                    body.x * BLOCK_SIZE,
                    body.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )

    def move(self, dx, dy):
        for idx in range(len(self.points) - 1, 0, -1):
            self.points[idx].x = self.points[idx - 1].x
            self.points[idx].y = self.points[idx - 1].y

        self.points[0].x += dx
        self.points[0].y += dy

        head = self.points[0]
        if head.x > WIDTH // BLOCK_SIZE:
            head.x = 0
        elif head.x < 0:
            head.x = WIDTH // BLOCK_SIZE - 1
        elif head.y > HEIGHT // BLOCK_SIZE:
            head.y = 0
        elif head.y < 0:
            head.y = HEIGHT // BLOCK_SIZE - 1


    def check_collision(self, food):
        if self.points[0].x != food.x:
            return False
        if self.points[0].y != food.y:
            return False
        return True


def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, GRID, (x, 0), (x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, GRID, (0, y), (WIDTH, y), width=1)


def main():
    running = True
    snake = Snake()
    food = Food(5, 5)
    dx, dy = 0, 0
    foods_eaten = 0
    speed = 3
    level = 1

    while running:
        SCREEN.fill(GRASS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    dx, dy = 0, -1
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, +1
                elif event.key == pygame.K_LEFT:
                    dx, dy = -1, 0
                elif event.key == pygame.K_RIGHT:
                    dx, dy = +1, 0

        score = score_font.render(f"Level:{str(level)}", True, (255, 0, 0))
        SCREEN.blit(score, (5, 0))

        snake.move(dx, dy)
        if snake.check_collision(food):
            snake.points.append(Point(food.x, food.y))
            food.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
            food.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
            foods_eaten += 1
            if foods_eaten == 1:
                speed += 0.1
                foods_eaten = 0
                level += 1

        food.update()
        snake.update()
        draw_grid()

        pygame.display.flip()
        clock.tick(speed)


if __name__ == '__main__':
    main()