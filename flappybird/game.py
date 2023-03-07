import pygame
import random
from pygame import mixer

class Bird:
    def __init__(self):
        pygame.init()
        self.xScreen, self.yScreen = 500, 600 # Screen create
        linkBackGround = './data/background.jpg'
        self.linkImgBird = './data/bird.jpg'
        self.screen = pygame.display.set_mode((self.xScreen, self.yScreen))
        pygame.display.set_caption("Code Learn - Fappybird")
        self.background = pygame.image.load(linkBackGround)
        self.gamerunning = True
        icon = pygame.image.load(self.linkImgBird)
        pygame.display.set_icon(icon)

        self.xSizeBird = 80 # Chieu cao bird
        self.ySizeBird = 60 # Chieu rong bird
        self.xBird = self.xScreen/3 # Vi tri ban dau
        self.yBird = self.yScreen/2 
        self.VBirdUp = 70 # Toc do nhay bird
        self.VBirdDown = 7 # Toc do roi bird

        self.xColunm = self.yScreen + 250 # Khoi tao cot dau tien
        self.yColunm = 0
        self.xSizeColunm = 100 # Chieu rong cot
        self.ySizeColunm = self.yScreen
        self.Vcolunm = 6 # Toc do di chuyen
        self.colunmChange = 0

        self.scores = 0
        self.checkLost = False
    
    def music(self, url): # Am thanh
        bulletSound = mixer.Sound(url)
        bulletSound.play()

    def image_draw(self, url, xLocal, yLocal, xImg, yImg): # In ra nguoi hinh anh
        PlanesImg = pygame.image.load(url)
        PlanesImg = pygame.transform.scale(
            PlanesImg, (xImg, yImg)
        ) # Change size image
        self.screen.blit(PlanesImg, (xLocal, yLocal))

    def show_score(self, x, y, scores, size): # Hien thi diem
        font = pygame.font.SysFont("comicsansms", size)
        score = font.render(str(scores), True, (255, 255, 255))
        self.screen.blit(score, (x, y))

    def colunm(self):
        maginColunm = 80
        yColunmChangeTop = -self.ySizeColunm/2 - maginColunm + \
            self.colunmChange # Khoang cach giua hai cot tren va duoi la 80*2
        yColunmChangeBotton = self.ySizeColunm /2 + maginColunm + self.colunmChange
        self.image_draw("./data/colunm.png", self.xColunm,
            yColunmChangeTop, self.xSizeColunm, self.xSizeColunm)
        self.image_draw("./data/colunm.png", self.xColunm,
            yColunmChangeBotton, self.xSizeColunm, self.ySizeColunm)
        self.xColunm = self.xColunm - self.Vcolunm
        if self.xColunm < -100: # Neu cot di qua man hinh
            self.xColunm = self.xScreen # Tao cot moi
            # Random khoang cach cot
            self.colunmChange = random.randint(-150, 150)
            self.scores +=1
        return yColunmChangeTop + self.ySizeColunm, yColunmChangeBotton
    
    def run(self):
        while self.gamerunning:
            self.screen.blit(self.background, (0, 0))
            for event in pygame.event.get(): # Bat cac su kien
            # print
            if event.type == pygame.QUIT: # Su kien nhan thoat
                self.gamerunning = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.yBird -= self.VBirdUp # Bird bay len
                self.music("./data/wet-click.wav")
            if event.type == pygame.KEYDOWN: # Su kien co phim nhan xuong
                if event.key == pygame.K_SPACE:
                    self.yBird -= self.VBirdUp # Bird bay len
                    self.music("./data/wet-click.wav")
        self.yBird += self.VBirdDown # Bird rot xuong
        yColunmChangeTop, yColunmChangeBotton = self.colunm()

        #====================Check xem bird cham cot ===============
        if self.yBird < yColunmChangeTop and (self.xColunm+self.xSizeColunm):
            self.checkLost = True
        if self.yBird + self.ySizeBird > yColunmChangeBotton and (self.xColunm):
            self.checkLost = True

        #============ Check xem bird cham tuong=======
        if (self.yBird + self.ySizeBird > self.yScreen) or self.yBird < 0:
            self.yBird = self.yScreen/2
            self.checkLost = True
        self.Vcolunm = 6 if self.scores < 1 else 6 + self.scores/5 # toc do
        self.VBirdDown = 7 if self.scores < 1 else 7 + self.scores/10 # bird roi nhanh
        print(self.Vcolunm)
        while(self.checkLost): # neu bird bi cham vat
            self.xColunm = self.xScreen + 100
            for event in pygame.event.get(): # Neu nhan
                if event.type == pygame.QUIT: # Thoat
                    self.gamerunning = False
                    self.checkLost = False
                    break
                if event.type == pygame.KEYDOWN: #Thoat
                    self.checkLost = False
                    self.scores = 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.checkLost = False
                    self.scores = 0
            self.show_score(100, 100, "Scores: {}".format(self.scores), 40) # In diem
            self.show_score(self.xScreen/2 - 100, self.yScreen/2 -100, "GAME OVER", 50) # In thong bao thua
            self.Vcolunm = 6
            self.VBirdDown = 7
            pygame.display.update()
        self.image_draw(self.linkImgBird, self.xBird, self.yBird, self,xSizeBird, self.yBird)
        self.show_score(self.xScreen - 200, 20, "hahahahah", 15)
        self.show_score(10, 10, "Scores: {}".format(self.scores), 35)
        pygame.display.update() # update
        clock = pygame.time.Clock()
        clock.tick(80)


if __name__ == "__main__":
    bird = Bird()
    bird.run()
