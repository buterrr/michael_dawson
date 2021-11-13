from livewires import games, color

WIDTH = 640
HEIGHT = 480

games.init(screen_width=WIDTH, screen_height=HEIGHT, fps=50)


class Pizza(games.Sprite):
    """ Скачущая пицца """

    def update(self):
        """ Обращает одну или обе компоненты скорости, если достигнута граница
        экрана """
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx
        if self.bottom > games.screen.height or self.top < 0:
            self.dy = -self.dy


def main():
    wall_image = games.load_image('img/wall.jpg', transparent=False)
    games.screen.background = wall_image
    pizza_image = games.load_image('img/pizza.bmp')
    pizza = Pizza(image=pizza_image,
                  x=WIDTH / 2,
                  y=HEIGHT / 2,
                  dx=1,
                  dy=1)
    games.screen.add(pizza)

    games.screen.mainloop()


main()
