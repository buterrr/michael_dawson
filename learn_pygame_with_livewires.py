from livewires import games, color
import random
WIDTH = 640
HEIGHT = 480

games.init(screen_width=WIDTH, screen_height=HEIGHT, fps=50)


class Pizza(games.Sprite):
    """ Ускользающая пицца. """
    def handle_collide(self):
        """ Пееремещает спрайт в случайную позицию на экране. """
        self.x = random.randrange(games.screen.width)
        self.y = random.randrange(games.screen.height)

    # def update(self):
    #     """ Обращает одну или обе компоненты скорости, если достигнута граница
    #     экрана """
    #     if self.right > games.screen.width or self.left < 0:
    #         self.dx = -self.dx
    #     if self.bottom > games.screen.height or self.top < 0:
    #         self.dy = -self.dy


class Pan(games.Sprite):
    """Перемещаемая мышью сковорода."""
    def update(self):
        """Перемещает объект в позицию указателя."""
        self.x = games.mouse.x
        self.y = games.mouse.y
        self.check_collide()

    def check_collide(self):
        """ Проверяет, не коснулись ли сковорода и пицца. """
        for pizza in self.overlapping_sprites:
            pizza.handle_collide()


def main():
    wall_image = games.load_image('img/wall.jpg', transparent=False)
    games.screen.background = wall_image
    pizza_image = games.load_image('img/pizza.bmp')
    pizza_x = random.randrange(WIDTH)
    pizza_y = random.randrange(HEIGHT)
    the_pizza = Pizza(image=pizza_image, x=pizza_x, y=pizza_y)
    games.screen.add(the_pizza)
    pan_image = games.load_image('img/pan.bmp')
    the_pan = Pan(image=pan_image,
                  x=games.mouse.x,
                  y=games.mouse.y)
    games.screen.add(the_pan)
    games.mouse.is_visible = False
    games.screen.event_grab = True

    games.screen.mainloop()


if __name__ == '__main__':
    main()
