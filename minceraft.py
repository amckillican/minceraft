from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

dirt = (load_texture("assets/block/dirt.png"), load_texture("assets/hotbar/dirt.png"))
stone = (load_texture("assets/block/stone.png"), load_texture("assets/hotbar/stone.png"))
bricks = (load_texture("assets/block/bricks.png"), load_texture("assets/hotbar/bricks.png"))
andesite = (load_texture("assets/block/andesite.png"), load_texture("assets/hotbar/andesite.png"))
granite = (load_texture("assets/block/granite.png"), load_texture("assets/hotbar/granite.png"))
diorite = (load_texture("assets/block/diorite.png"), load_texture("assets/hotbar/diorite.png"))
bedrock = (load_texture("assets/block/bedrock.png"), load_texture("assets/hotbar/bedrock.png"))
sky_texture = load_texture("assets/skybox.png")
arm_texture = load_texture("assets/arm/arm_texture.png")
hotbar_texture = (dirt[1], stone[1], bricks[1], andesite[1], granite[1], diorite[1], bedrock[1])
block_pick = 1


window.fps_counter.enabled = False
window.exit_button.enabled = False


def update():
    global block_pick
    if held_keys["1"]: block_pick = 1
    if held_keys["2"]: block_pick = 2
    if held_keys["3"]: block_pick = 3
    if held_keys["4"]: block_pick = 4
    if held_keys["5"]: block_pick = 5
    if held_keys["6"]: block_pick = 6
    if held_keys["7"]: block_pick = 7

    if held_keys["left mouse"] or held_keys["right mouse"]:
        hand.active()
    else:
        hand.passive()


class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=dirt[0]):
        super().__init__(
            parent=scene,
            position=position,
            model="cube",
            origin_y=0.5,
            texture=texture,
            color=color.white)

    def input(self, key):
        if self.hovered:
            if key == "right mouse down":
                if block_pick == 1:
                    voxel = Voxel(position=self.position + mouse.normal, texture=dirt[0])
                elif block_pick == 2:
                    voxel = Voxel(position=self.position + mouse.normal, texture=stone[0])
                elif block_pick == 3:
                    voxel = Voxel(position=self.position + mouse.normal, texture=bricks[0])
                elif block_pick == 4:
                    voxel = Voxel(position=self.position + mouse.normal, texture=andesite[0])
                elif block_pick == 5:
                    voxel = Voxel(position=self.position + mouse.normal, texture=granite[0])
                elif block_pick == 6:
                    voxel = Voxel(position=self.position + mouse.normal, texture=diorite[0])
                elif block_pick == 7:
                    voxel = Voxel(position=self.position + mouse.normal, texture=bedrock[0])

            if key == "left mouse down":
                destroy(self)


class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model="sphere",
            texture=sky_texture,
            scale=150,
            double_sided=True)


class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model="assets/arm/arm.obj",
            texture=arm_texture,
            scale=0.205,
            rotation=Vec3(145, -20, 0),
            position=Vec2(0.75, -0.6))

    def active(self):
        self.position = Vec2(0.55, -0.5)

    def passive(self):
        self.position = Vec2(0.75, -0.6)


class Hotbar(Entity):
    def __init__(self, texture = dirt[1]):
        super().__init__(
            parent=camera.ui,
            model="quad",
            texture=hotbar_texture[block_pick-1],
            scale=0.07,
            position=Vec2(0, -0.465),
            scale_x=.44)


size = 10
height = 3
for z in range(size):
    for x in range(size):
        for y in range(height + 1):
            if y == 0:
                voxel = Voxel(position=(x, -y, z), texture=dirt[0])
            elif y < height:
                voxel = Voxel(position=(x, -y, z), texture=stone[0])
            elif y == height:
                voxel = Voxel(position=(x, -y, z), texture=bedrock[0])

player = FirstPersonController()
sky = Sky()
hand = Hand()
hotbar = Hotbar()

app.run()
