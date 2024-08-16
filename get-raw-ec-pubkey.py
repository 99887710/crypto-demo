# EXAMPLE PUBLIC KEY 

# -----BEGIN PUBLIC KEY-----
# MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEQDGTIrEGd2cXAKiGg9VFI1jvCDx0
# 9hEcOgfzfredbBKvMd3gqyuC8Xgd0KpPXo7XdbizTTjUcw4tjYIfCj1cyw==
# -----END PUBLIC KEY-----

# Convert pem to hex
# https://holtstrom.com/michael/tools/hextopem.php
# https://holtstrom.com/michael/tools/asn1decoder.php
derPublic = '3059301306072A8648CE3D020106082A8648CE3D0301070342000440319322B10677671700A88683D5452358EF083C74F6111C3A07F37EB79D6C12AF31DDE0AB2B82F1781DD0AA4F5E8ED775B8B34D38D4730E2D8D821F0A3D5CCB'

# Retrive first 54 chars as raw public key has 128 hex chars
# len(derPubKey) 182 = p256-Head + x-cooordinate + y-cooordinate 
# len(rawPubKey) 128 = x-cooordinate + y-cooordinate 
# 182 - 128 = 54
p256_head = derPublic[:54]
print(p256_head)

# Output: 3059301306072A8648CE3D020106082A8648CE3D03010703420004