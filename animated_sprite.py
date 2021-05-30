import os

import pygame


class AnimatedSprite:
    def __init__(
        self,
        folder,
        file,
        end,
        start=1,
        fps=3,
        file_type="png",
        flipX=False,
        flipY=False,
    ):
        self.curImage = start - 1
        self.folder = folder
        self.file = file
        self.end = end
        self.file_type = file_type
        self.flipX = flipX
        self.flipY = flipY

        self.fps = fps
        self.max_image = self.fps * end
        self.images = []

        for i in range(self.curImage + 1, self.end + 1):
            path = os.path.join(self.folder, f"{self.file}{i}.{self.file_type}")
            self.images.append(pygame.image.load(path))

    def draw(self, screen, pos):
        """
        Blits the current animation into screen
        """
        if self.curImage + 1 >= self.max_image:
            self.curImage = 0
        self.curImage += 1
        screen.blit(
            pygame.transform.flip(
                self.images[(self.curImage // self.fps) - 1], self.flipX, self.flipY
            ),
            pos,
        )
