# Builds the farm tile map and writes it as JS.
W, H, G = 120, 44, 27
g = [['.'] * W for _ in range(H)]

def R(x0, y0, x1, y1, c):
    for y in range(min(y0, y1), max(y0, y1) + 1):
        for x in range(min(x0, x1), max(x0, x1) + 1):
            if 0 <= x < W and 0 <= y < H:
                g[y][x] = c

R(0, G, W - 1, H - 1, '#')                      # earth

# ---------- HOUSE (x 3..18) ----------
R(3, 19, 3, 26, 'B'); R(18, 19, 18, 26, 'B')    # walls
for i in range(5):                               # stepped roof, climbable like stairs
    R(3 + i, 18 - i, 19 - i, 18 - i, 'R')
R(13, 12, 14, 13, 'S')                           # chimney
R(18, 25, 18, 26, '.')                           # front door (east)
R(18, 21, 18, 22, '.')                           # upstairs window (east)
R(4, 23, 17, 23, '=')                            # upper floor (reaches the window)
R(14, 25, 15, 25, '=')                           # chair
# cellar under the house
R(3, 27, 18, 37, 'B'); R(4, 28, 17, 36, '.')
R(4, 27, 17, 27, '#')                            # house floor = ground
R(6, 27, 7, 27, '.')                             # trapdoor
R(5, 29, 8, 36, 'B')                             # landing under the trapdoor
for i in range(7):                               # stairs down to the cellar floor
    R(9 + i, 30 + i, 9 + i, 36, 'B')
R(16, 35, 17, 36, 'o')                           # barrels
R(16, 33, 17, 33, '=')                           # shelf
R(18, 35, 18, 36, '.')                           # cellar door to the tunnel
# west chimney: crates next to the map edge, wall-jump up to the roof
R(0, 25, 1, 26, 'x')

# ---------- YARD, SHED, TREE, WELL (x 19..34) ----------
R(19, 23, 24, 23, '=')                           # shed roof
R(23, 25, 24, 26, 'x')                           # firewood crates
R(21, 21, 24, 21, '-')                           # tree branch A
R(20, 19, 22, 19, '-')                           # tree branch B (reaches the house eave)
R(27, 25, 27, 26, 'S'); R(30, 25, 30, 26, 'S')   # well rim
R(28, 23, 29, 23, '=')                           # bucket
R(26, 21, 31, 21, '=')                           # well roof
R(27, 27, 27, 36, 'S'); R(30, 27, 30, 36, 'S')   # shaft lining (reaches into the cave)
R(28, 27, 29, 36, '.')                           # shaft

# ---------- BARN (x 35..59) ----------
R(36, 15, 36, 26, 'W'); R(58, 15, 58, 26, 'W')
for i in range(7):
    R(35 + i, 14 - i, 59 - i, 14 - i, 'R')
R(58, 23, 58, 26, '.')                           # big door (east)
R(58, 19, 58, 20, '.')                           # loft door
R(37, 21, 47, 21, '='); R(51, 21, 57, 21, '=')   # haylofts
R(44, 25, 47, 26, 'H'); R(46, 23, 47, 24, 'H')   # bales up to the west loft
R(39, 19, 40, 20, 'H'); R(54, 19, 55, 20, 'H')   # bales on the lofts
R(42, 17, 51, 17, '=')                           # rafters
R(46, 8, 47, 14, '.')                            # roof hatch shaft
R(59, 21, 61, 21, '=')                           # pulley beam outside the loft door
R(32, 16, 33, 26, 'H')                           # tall hay tower (wall-jump chimney with the barn)
R(30, 25, 31, 26, 'H')                           # small bales

# ---------- ORCHARD + COOP (x 60..79) ----------
for (y, a, b) in [(25, 61, 63), (23, 64, 66), (21, 62, 62), (19, 63, 65), (17, 60, 62), (15, 60, 62), (13, 63, 64)]:
    R(a, y, b, y, '-')
R(70, 23, 75, 26, 'W'); R(71, 23, 74, 26, '.')   # coop
R(69, 22, 76, 22, 'R')                           # coop roof
R(70, 25, 70, 26, '.'); R(75, 25, 75, 26, '.')   # two coop doors
R(73, 25, 74, 25, '=')                           # nest
R(77, 25, 78, 26, 'x'); R(78, 23, 78, 24, 'x')   # crates up to the coop roof

# ---------- POND (x 80..95) ----------
R(81, G, 94, 31, '~')
R(87, 26, 88, 31, 'r')                           # island
R(83, 26, 84, 26, '=')                           # floating log

# ---------- MEADOW + HILL (x 96..119) ----------
R(97, 25, 102, 25, 'f')                          # fence rail
hill = {101: 26, 102: 25, 103: 24, 104: 23, 111: 21, 112: 20}
for x in range(101, W):
    top = hill.get(x, 22 if x <= 110 else 19)
    R(x, top, x, 26, '#')
R(116, 17, 117, 18, 'r')                         # lookout rock
R(103, 25, 104, 26, '.')                         # hill cave mouth
R(105, 23, 108, 35, '.')                         # mouth shaft down into the hill
for (y, a) in [(34, 107), (32, 105), (30, 107), (28, 105)]:
    R(a, y, a + 1, y, 'S')
R(109, 29, 116, 30, '.')                         # chamber
R(113, 19, 114, 28, '.')                         # chimney up to the hilltop

# ---------- UNDERGROUND ----------
R(19, 35, 25, 36, '.')                           # tunnel cellar -> well cave
R(24, 33, 36, 39, '.')                           # well cave
R(27, 33, 27, 36, 'S'); R(30, 33, 30, 36, 'S')   # well pipe hangs into the cave
R(26, 38, 33, 39, '~')                           # pool under the well
R(24, 39, 24, 39, 'S')                           # step up to the tunnel
R(34, 37, 35, 37, 'S'); R(36, 39, 36, 39, 'S')   # ledge + step
R(37, 35, 59, 37, '.')                           # long tunnel east
R(60, 30, 80, 40, '.')                           # big cave
R(60, 38, 60, 40, '#'); R(61, 40, 61, 40, 'S')   # ledge back into the tunnel
for (y, a) in [(38, 64), (36, 68), (34, 64), (32, 68)]:
    R(a, y, a + 2, y, 'S')
R(75, 31, 75, 36, 'S')                           # stalactite pillar
R(81, 36, 85, 37, '.')                           # passage to the lake
R(82, 34, 96, 40, '.')                           # lake cave
R(86, 38, 96, 40, '~')                           # lake
R(81, 38, 81, 40, '#'); R(82, 40, 82, 40, 'S'); R(80, 40, 80, 40, 'S')
R(96, 33, 104, 35, '.')                          # passage up to the hill
R(96, 36, 96, 37, '#')                           # lip to climb out of the lake
R(105, 36, 108, 36, '#')

TREATS = [(13.5, 11), (4.5, 22), (16.5, 32), (28.5, 20), (35, 36), (55, 18), (52, 7), (64, 12), (73.5, 24), (87.5, 25), (69, 31), (116.5, 16)]
for (x, y) in TREATS:
    assert g[int(y)][int(x)] in '.', ('treat inside solid', x, y, g[int(y)][int(x)])

rows = [''.join(r) for r in g]
REGIONS = [
    ('house', 4, 19, 17, 26), ('cellar', 4, 28, 17, 36), ('barn', 37, 15, 57, 26), ('barn', 46, 8, 47, 14),
    ('barn', 71, 23, 74, 26), ('cave', 103, 23, 108, 26), ('cave', 113, 19, 114, 28),
]
import json
js = 'const FARM={W:%d,H:%d,G:%d,rows:%s,treats:%s,regions:%s,start:[24,%d]};\n' % (
    W, H, G, json.dumps(rows), json.dumps(TREATS), json.dumps(REGIONS), G)
open('/tmp/claude-0/farm_map.js', 'w').write(js)
print('\n'.join(rows))
