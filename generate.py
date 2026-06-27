flowers = [
    ('sunflower', '--x: 50%; --y: 5%; --r: 0deg; --s: 1; --h: 24em; --d: 1s; --z: 15;', 'sway--1', '<div class="petal"></div>'*16 + '<div class="center"><div class="center-inner"></div></div><div class="flower__light flower__light--1"></div><div class="flower__light flower__light--2"></div><div class="flower__light flower__light--3"></div><div class="flower__light flower__light--4"></div>', '<div class="flower__line__leaf flower__line__leaf--1"></div><div class="flower__line__leaf flower__line__leaf--3"></div><div class="flower__line__leaf flower__line__leaf--5"></div>'),
    ('sunflower', '--x: 55%; --y: 6%; --r: 15deg; --s: 0.85; --h: 22em; --d: 1.5s; --z: 14;', 'sway--2', '<div class="petal"></div>'*16 + '<div class="center"><div class="center-inner"></div></div><div class="flower__light flower__light--5"></div><div class="flower__light flower__light--6"></div>', '<div class="flower__line__leaf flower__line__leaf--2"></div><div class="flower__line__leaf flower__line__leaf--4"></div>'),
    ('sunflower', '--x: 45%; --y: 6%; --r: -15deg; --s: 0.85; --h: 23em; --d: 1.8s; --z: 13;', 'sway--3', '<div class="petal"></div>'*16 + '<div class="center"><div class="center-inner"></div></div><div class="flower__light flower__light--7"></div><div class="flower__light flower__light--8"></div>', '<div class="flower__line__leaf flower__line__leaf--1"></div><div class="flower__line__leaf flower__line__leaf--4"></div>'),
    ('tulip tulip-pink', '--x: 48%; --y: 8%; --r: -5deg; --s: 0.8; --h: 18em; --d: 1.2s; --z: 12;', 'sway--1', '<div class="petal petal-left"></div><div class="petal petal-center"></div><div class="petal petal-right"></div>', '<div class="tulip-leaf-l"></div>'),
    ('tulip tulip-red', '--x: 58%; --y: 10%; --r: 25deg; --s: 0.8; --h: 17em; --d: 2.1s; --z: 11;', 'sway--2', '<div class="petal petal-left"></div><div class="petal petal-center"></div><div class="petal petal-right"></div>', '<div class="flower__line__leaf flower__line__leaf--3"></div>'),
    ('tulip tulip-pink', '--x: 42%; --y: 10%; --r: -25deg; --s: 0.75; --h: 16em; --d: 2.4s; --z: 10;', 'sway--3', '<div class="petal petal-left"></div><div class="petal petal-center"></div><div class="petal petal-right"></div>', '<div class="tulip-leaf-l"></div>'),
    ('tulip tulip-red', '--x: 52%; --y: 12%; --r: 8deg; --s: 0.85; --h: 19em; --d: 1.7s; --z: 16;', 'sway--1', '<div class="petal petal-left"></div><div class="petal petal-center"></div><div class="petal petal-right"></div>', '<div class="flower__line__leaf flower__line__leaf--3"></div>'),
    ('daisy', '--x: 40%; --y: 12%; --r: -35deg; --s: 0.7; --h: 15em; --d: 1.6s; --z: 9;', 'sway--2', '<div class="petal"></div>'*12 + '<div class="center"></div>', '<div class="flower__line__leaf flower__line__leaf--4"></div><div class="flower__line__leaf flower__line__leaf--2"></div>'),
    ('daisy', '--x: 60%; --y: 12%; --r: 35deg; --s: 0.7; --h: 14em; --d: 2.3s; --z: 8;', 'sway--3', '<div class="petal"></div>'*12 + '<div class="center"></div>', '<div class="flower__line__leaf flower__line__leaf--1"></div>'),
    ('daisy', '--x: 46%; --y: 8%; --r: -10deg; --s: 0.75; --h: 17em; --d: 2.6s; --z: 17;', 'sway--1', '<div class="petal"></div>'*12 + '<div class="center"></div>', '<div class="flower__line__leaf flower__line__leaf--4"></div>'),
    ('daisy', '--x: 54%; --y: 8%; --r: 10deg; --s: 0.75; --h: 16em; --d: 1.4s; --z: 18;', 'sway--2', '<div class="petal"></div>'*12 + '<div class="center"></div>', '<div class="flower__line__leaf flower__line__leaf--2"></div>'),
    ('daisy', '--x: 50%; --y: 20%; --r: 0deg; --s: 0.8; --h: 12em; --d: 2.8s; --z: 19;', 'sway--3', '<div class="petal"></div>'*12 + '<div class="center"></div>', '<div class="flower__line__leaf flower__line__leaf--1"></div>'),
    ('orchid', '--x: 43%; --y: 10%; --r: -20deg; --s: 0.8; --h: 14em; --d: 1.9s; --z: 20;', 'sway--1', '<div class="sepal sepal-top"></div><div class="sepal sepal-left"></div><div class="sepal sepal-right"></div><div class="inner-petal inner-left"></div><div class="inner-petal inner-right"></div><div class="lip"></div><div class="column"></div><div class="flower__light flower__light--1"></div>', '<div class="flower__line__leaf flower__line__leaf--5"></div>'),
    ('orchid', '--x: 57%; --y: 10%; --r: 20deg; --s: 0.8; --h: 13em; --d: 2.5s; --z: 21;', 'sway--2', '<div class="sepal sepal-top"></div><div class="sepal sepal-left"></div><div class="sepal sepal-right"></div><div class="inner-petal inner-left"></div><div class="inner-petal inner-right"></div><div class="lip"></div><div class="column"></div><div class="flower__light flower__light--2"></div>', '<div class="flower__line__leaf flower__line__leaf--6\"></div>'),
    ('orchid', '--x: 50%; --y: 15%; --r: 5deg; --s: 0.75; --h: 15em; --d: 2.9s; --z: 22;', 'sway--3', '<div class="sepal sepal-top"></div><div class="sepal sepal-left"></div><div class="sepal sepal-right"></div><div class="inner-petal inner-left"></div><div class="inner-petal inner-right"></div><div class="lip"></div><div class="column"></div><div class="flower__light flower__light--3"></div>', '<div class="flower__line__leaf flower__line__leaf--5"></div>'),
    ('orchid', '--x: 50%; --y: 15%; --r: 5deg; --s: 0.75; --h: 15em; --d: 2.9s; --z: 22;', 'sway--3', '<div class="sepal sepal-top"></div><div class="sepal sepal-left"></div><div class="sepal sepal-right"></div><div class="inner-petal inner-left"></div><div class="inner-petal inner-right"></div><div class="lip"></div><div class="column"></div><div class="flower__light flower__light--3"></div>', '<div class="flower__line__leaf flower__line__leaf--5"></div>'),
    ('daisy', '--x: 35%; --y: 15%; --r: -45deg; --s: 0.65; --h: 13em; --d: 3.2s; --z: 7;', 'sway--1', '<div class="petal"></div>'*12 + '<div class="center"></div>', '<div class="flower__line__leaf flower__line__leaf--1"></div>'),
    ('tulip tulip-red', '--x: 65%; --y: 15%; --r: 45deg; --s: 0.7; --h: 14em; --d: 3.5s; --z: 6;', 'sway--2', '<div class="petal petal-left"></div><div class="petal petal-center"></div><div class="petal petal-right"></div>', '<div class="flower__line__leaf flower__line__leaf--3"></div>')
]

out = ""
for c, st, sw, leafs, stem in flowers:
    out += f"""
                <div class="flower {c}" style="{st}">
                    <div class="flower__sway {sw}">
                        <div class="flower__leafs">
                            {leafs}
                        </div>
                        <div class="flower__line">
                            {stem}
                        </div>
                    </div>
                </div>"""

with open('out.html', 'w', encoding='utf-8') as f:
    f.write(out)
print('Done!')
