
import pygame as pg
from pygame.locals import *
from sys import exit

pg.init()
screensize = (1200, 800)
screen = pg.display.set_mode(screensize)
caption = pg.image.load("lala.png")
pg.display.set_icon(caption)

scheme = pg.image.load("PONUR.png")
pg.display.set_caption("SOLVMRF - SOLID WASTE MENAGEMENT TERM PROJECT")
intro = pg.image.load('YUNUS.png')
screen.fill((40, 40, 40))
screen.blit(scheme, (2, 0))
Q = []
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 30)
red = (255, 0, 0)
green = (0, 128, 0)
memb = False
disn = False



class InputBox:

    def __init__(self, x, y, w, h, text='', *a):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    if self.text != '' and len(Q) <= 6:
                        Q.append(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        width = max(80, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)

def blitter():

    screen.blit(mass_inp, fr_coord)
    screen.blit(aim_wr, aim_coord)
    screen.blit(x_wr, x_coord)
    screen.blit(z_wr, z_coord)
    screen.blit(h_wr, h_coord)
    screen.blit(p_wr, p_coord)


def calculator(mass_in,paper,glass,non_ferrus,ferrus,plastic,):
    myfont = pg.font.Font(None, 30)
    paper_mass = (mass_in/100)*paper
    glass_mass = (mass_in/100)*glass
    ferrus_mass = (mass_in/100)*ferrus
    nonferrus_mass = (mass_in/100)*non_ferrus
    plastic_mass = (mass_in/100)*plastic

    #after trommel send
    post_trom_paper = paper_mass * 0.95
    post_trom_glass = glass_mass * 0.95
    post_trom_ferrus = ferrus_mass * 0.95
    post_trom_nonferrus = nonferrus_mass * 0.95
    post_trom_plastic = plastic_mass * 0.95


    #after trommel to the landfill

    trom_to_landfill_mass = (paper_mass + glass_mass  + ferrus_mass + nonferrus_mass + plastic_mass)*0.05

    #sorting seperated

    sort_sep_paper = post_trom_paper*0.8
    sort_sep_plastic = post_trom_plastic*0.8

    sorted_mass = sort_sep_paper + sort_sep_plastic

    #sorting send
    post_sort_paper = post_trom_paper*0.2
    post_sort_glass = post_trom_glass
    post_sort_ferrus = post_trom_ferrus
    post_sort_nonferrus = post_trom_nonferrus
    post_sort_plastic = post_trom_plastic*0.2
    mass_sort_send = post_sort_ferrus + post_sort_glass + post_sort_nonferrus + post_sort_paper + post_sort_plastic

    #magnetic seperator seperated
    magn_sep_ferrus = post_trom_ferrus*0.98


    #magnetic seperator send
    post_magn_paper = post_sort_paper
    post_magn_glass = post_sort_glass
    post_magn_ferrus = post_sort_ferrus*0.02
    post_magn_nonferrus = post_sort_nonferrus
    post_magn_plastic = post_sort_plastic

    mass_magn_send = post_magn_ferrus + post_magn_glass + post_magn_paper + post_magn_nonferrus + post_magn_plastic

    #eddy current seperator
    edd_curr_sep = post_magn_nonferrus*0.97

    #eddy current send
    
    post_eddy_paper = post_magn_paper
    post_eddy_glass = post_magn_glass
    post_eddy_ferrus = post_magn_ferrus
    post_eddy_nonferrus = post_magn_nonferrus*0.03
    post_eddy_plastic = post_magn_plastic
    mass_eddy_send = post_eddy_paper + post_eddy_glass + post_eddy_ferrus + post_eddy_nonferrus + post_eddy_plastic
    
    #vibrating seperator
    vibr_sep_glass = post_eddy_glass*0.6
    
    #vibrating to landfill
    vibr_landfill_paper = post_eddy_paper
    vibr_landfill_glass = post_eddy_glass*0.4
    vibr_landfill_ferrus = post_eddy_ferrus
    vibr_landfill_nonferrus = post_eddy_nonferrus
    vibr_landfill_plastic = post_eddy_plastic
    
    vibr_to_landfill = vibr_landfill_ferrus + vibr_landfill_glass + vibr_landfill_nonferrus + vibr_landfill_paper + vibr_landfill_plastic
    
    #optical_seperation
    opt_sep_glass = vibr_sep_glass*0.98
    
    #optical seperation to landfill
    opt_rej_glass = vibr_sep_glass*0.02

    trom_result_land = myfont.render('{} Tons'.format(round(trom_to_landfill_mass, 3)), False, (0, 0, 0))
    sort_result_paper = myfont.render('Paper Sep. : {} Tons '.format(round(sort_sep_paper,3)), False, (0, 0, 0))
    sort_result_plast = myfont.render('Plastic Sep. : {} Tons'.format(round(sort_sep_plastic,3)), False, (0, 0, 0))
    magn_result_ferr = myfont.render('Metals Sep. : {} Tons'.format(round(sort_sep_paper,3)), False, (0, 0, 0))
    edd_result_nonferr = myfont.render('NF Metals Sep. : {} Tons'.format(round(edd_curr_sep,3)), False, (0, 0, 0))
    vib_result_glass = myfont.render('Glass: {} Tons'.format(round(vibr_sep_glass,3)), False, (0, 0, 0))
    opt_result_glass = myfont.render('Glass Sep.: {} Tons'.format(round(opt_sep_glass,3)), False, (0, 0, 0))
    vib_result_landfill = myfont.render('{} Tons'.format(round(vibr_to_landfill,3)),False,(0,0,0))
    m1_result = myfont.render('{} Tons'.format(round(mass_in*0.95, 3)), False, (0, 0, 0))
    m2_result = myfont.render('{} Tons'.format(round(mass_sort_send, 3)), False, (0, 0, 0))
    m3_result = myfont.render('{} Tons'.format(round(mass_magn_send, 3)), False, (0, 0, 0))
    m4_result = myfont.render('{} Tons'.format(round(mass_eddy_send, 3)), False, (0, 0, 0))
    m5_result = myfont.render('{} Tons'.format(round(opt_rej_glass, 3)), False, (0, 0, 0))
    m6_result = myfont.render('{} Tons'.format(round(mass_in*0.05 + vibr_to_landfill + opt_rej_glass, 3)), False, (0, 0, 0))

    landfill_paper = myfont.render('Paper: {} Tons'.format(round(paper_mass * 0.05 + paper_mass*0.95*0.2, 3)), False, (0, 0, 0))
    landfill_glass = myfont.render('Glass: {} Tons'.format(round(glass_mass*0.05 +glass_mass*0.95*0.4 + glass*0.95*0.02*0.6, 3) + opt_rej_glass), False, (0, 0, 0))
    landfill_ferrus = myfont.render('F Metal: {} Tons'.format(round(ferrus_mass*0.05 + ferrus_mass*0.95*0.02, 3)), False, (0, 0, 0))
    landfill_nonferrus = myfont.render('NF Metal: {} Tons'.format(round(nonferrus_mass*0.05 + nonferrus_mass*0.95*0.003, 3)), False, (0, 0, 0))
    landfill_plastic = myfont.render('Plastic: {} Tons'.format(round(plastic_mass*0.05 + plastic_mass*0.95*0.2, 3)), False, (0, 0, 0))


    # coordinates of units
    trom_x = 127
    trom_y = 220

    sort_x = 606
    sort_y = 156

    magn_x = 887
    magn_y = 156

    edd_x = 865
    edd_y = 467

    vib_x = 646
    vib_y = 513

    vib_land_x = 403
    vib_land_y = 436

    opt_x = 516
    opt_y = 665
    # trommel reject coord

    # trommel permeate coord
    mass1_x = 482
    mass1_y = 71
    # sorting yield coord
    mass2_x = 790
    mass2_y = 71
    # eddy current seperator yield
    mass3_x =1040
    mass3_y = 275


    mass4_x = 769
    mass4_y = 396
    # optical sort rejectate
    mass5_x = 403
    mass5_y = 643
    # landfill overall
    mass6_x = 634
    mass6_y = 742

    # landfill composition
    land_x = 970
    land_y = 660

    screen.blit(sort_result_paper,(sort_x,sort_y))
    screen.blit(sort_result_plast,(sort_x,sort_y + 25))
    screen.blit(magn_result_ferr,(magn_x,magn_y))
    screen.blit(edd_result_nonferr,(edd_x,edd_y))
    screen.blit(vib_result_glass,(vib_x,vib_y))
    screen.blit(opt_result_glass,(opt_x,opt_y))

    screen.blit(trom_result_land,(trom_x+110,trom_y + 55))
    screen.blit(vib_result_landfill,(vib_land_x,vib_land_y))
    screen.blit(m1_result,(mass1_x,mass1_y))
    screen.blit(m2_result, (mass2_x, mass2_y))
    screen.blit(m3_result, (mass3_x, mass3_y))
    screen.blit(m4_result, (mass4_x, mass4_y))
    screen.blit(m5_result, (mass5_x, mass5_y))
    screen.blit(m6_result , (mass6_x, mass6_y))
    screen.blit(landfill_ferrus,(land_x,land_y))

    screen.blit(landfill_glass,(land_x,land_y+25))
    screen.blit(landfill_nonferrus,(land_x,land_y + 50))
    screen.blit(landfill_paper,(land_x,land_y + 75))
    screen.blit(landfill_plastic,(land_x,land_y + 100))


    pg.display.update()


c_intro = True

pg.font.init()
screen.blit(scheme, (2, 0))
myfont = pg.font.Font(None, 30)
mass_inp = myfont.render('Total Mass                      (Tons) ', False, (255, 0, 0))
aim_wr = myfont.render('%Paper: ', False, (255, 0, 0))
x_wr = myfont.render('%Glass: ', False, (255, 0, 0))
z_wr = myfont.render('%NF Metals: ', False, (255, 0, 0))
h_wr = myfont.render('%F Metals: ', False, (255, 0, 0))
p_wr = myfont.render('%Plastic:', False, (255, 0, 0))
    ## results printouts


fr_coord = (15, 500)
aim_coord = (15, 550)
x_coord = (15, 600)
z_coord = (15, 650)
h_coord = (15, 700)
p_coord = (15, 750)
screen.blit(mass_inp, fr_coord)
screen.blit(aim_wr, aim_coord)
screen.blit(x_wr, x_coord)
screen.blit(z_wr, z_coord)
screen.blit(h_wr, h_coord)
screen.blit(p_wr, p_coord)
pg.display.update()
box_w = 80
box_l = 30
flow_input = InputBox(165, 500, box_w, box_l)
aim_input = InputBox(165, 550, box_w, box_l)
x_input = InputBox(165, 600, box_w, box_l)
z_input = InputBox(165, 650, box_w, box_l)
h_input = InputBox(165, 700, box_w, box_l)
p_input = InputBox(165, 750, box_w, box_l)
input_boxes = [flow_input, aim_input, x_input, z_input, h_input, p_input]
done = False
i = 0
EqFl = 0
EqAim = 0
EqX = 0
EqZ = 0
colch = 0
reset = True


while c_intro:
    pg.display.update()
    screen.blit(intro,[0,0])
    for event in pg.event.get():
        screen.blit(intro, (0, 0))
        if event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN:
            c_intro = False
            break
        if event.type == pg.QUIT:
            exit()
            pg.quit()

            break


screen.blit(scheme,(0,2))
#calculator(200,20,20,20,20,20)
GAGA = True
while GAGA:

    if c_intro:
        screen.blit(intro, (0, 0))
        for event in pg.event.get():
            screen.blit(intro, (0, 0))
            if event.type == pg.KEYDOWN:
                c_intro = False

                blitter()
    if not reset and p:
        pg.font.init()

        myfont = pg.font.Font(None, 30)
        mass_inp = myfont.render('Total Mass                      (Tons) ', False, (255, 0, 0))
        aim_wr = myfont.render('%Paper: ', False, (255, 0, 0))
        x_wr = myfont.render('%Glass: ', False, (255, 0, 0))
        z_wr = myfont.render('%NF Metals: ', False, (255, 0, 0))
        h_wr = myfont.render('%F Metals: ', False, (255, 0, 0))
        p_wr = myfont.render('%Plastic:', False, (255, 0, 0))

        blitter()

        fr_coord = (15, 500)
        aim_coord = (15, 550)
        x_coord = (15, 600)
        z_coord = (15, 650)
        h_coord = (15, 700)
        p_coord = (15, 750)
        screen.blit(mass_inp, fr_coord)
        screen.blit(aim_wr, aim_coord)
        screen.blit(scheme,(2,0))
        screen.blit(x_wr, x_coord)
        screen.blit(z_wr, z_coord)
        screen.blit(h_wr, h_coord)
        screen.blit(p_wr, p_coord)
        pg.display.update()
        box_w = 80
        box_l = 30
        flow_input = InputBox(165, 500, box_w, box_l)
        aim_input = InputBox(165, 550, box_w, box_l)
        x_input = InputBox(165, 600, box_w, box_l)
        z_input = InputBox(165, 650, box_w, box_l)
        h_input = InputBox(165, 700, box_w, box_l)
        p_input = InputBox(165, 750, box_w, box_l)
        input_boxes = [flow_input, aim_input, x_input, z_input, h_input, p_input]
        done = False
        i = 0
        EqFl = 0
        EqAim = 0
        EqX = 0
        EqZ = 0
        colch = 0
        reset = True
        screen.blit(scheme, (0, 2))
        Q = []
        ## results printouts


    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
            pg.quit()
            GAGA = False

            break
        #screen.blit(scheme,(0,2))
        blitter()
        if event.type == pg.KEYDOWN:
            if event.key == K_r:
                reset = not reset
                p = True
                continue
        if event.type == pg.MOUSEBUTTONDOWN:

            xcl = event.pos[0]
            ycl = event.pos[1]

        for box in input_boxes:
            box.handle_event(event)
        change = False

        for box in input_boxes:
            box.update()
    try:
        mass_in = float(Q[0])
        EqPa = float(Q[1])
        EqX = float(Q[2])
        EqZ = float(Q[3])
        EqH = float(Q[4])
        EqP = float(Q[5])
        i += 1
        if i <= 1:


            calculator(mass_in,EqPa,EqX,EqZ,EqH,EqP)
    except:
        pass
    for box in input_boxes:
        box.draw(screen)

    pg.display.flip()
