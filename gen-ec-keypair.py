# derive the public key from the private key:
# The public key is the resulting point of the scalar multiplication or sG

from pycoin.ecdsa import generator_secp256k1 as g
secret = 7
x, y = (secret*g).pair()
print(hex(x), hex(y))

# 0x9680241112d370b56da22eb535745d9e314380e568229e09f7241066003bc471 0xddac2d377f03c201ffa0419d6596d10327d6c70313bb492ff495f946285d8f38