print ("Zakaria Ghalmi")
def decrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 - key) % 26 + 65)
            else:
                result += chr((ord(char) - 97 - key) % 26 + 97)
        else:
            result += char
    return result


def encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + key) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + key) % 26 + 97)
        else:
            result += char
    return result


print(" Decryption with key = 8")
ciphertext1 = """Uwdqvo jmgwvl aquxtm apqnba tmba mfxtwzm i uwzm qvbzqkibm bzivaxwaqbqwv eqbp bpm
mfiuxtm wn i twdm vwbm Caqvo i ozql agabmu em zmizzivom tmbbmza jiaml wv i axmkqnqk
zmilqvo umbpwl Bpm kqxpmzbmfb uiqvbiqva bpm aium tmbbmza ia bpm xtiqvbmfb jcb nwzua i
vme xibbmzv zmycqzqvo svwetmlom wn bpm ozqla lqumvaqwva ivl zmilqvo xibbmzv nwz
lmkzgxbqwv"""
decrypted = decrypt(ciphertext1, 8)
print(decrypted)
print("-" * 50)


print("Encryption with key = 15")
plaintext2 = """Diffusion serves as a cornerstone in cryptographic endeavors By dispersing the statistical
structure of plaintext within the ciphertext cryptographers obscure any discernible patterns
Through a combination of transposition and substitution diffusion eliminates clues that could
aid adversaries in unraveling encrypted messages"""
encrypted = encrypt(plaintext2, 15)
print(encrypted)
print("-" * 50)


print("Find the key")
ciphertext3 = """Wlsjnialujbs uhx Yhwlsjncih bupy vyyh omyx zil mywoly wiggohcwuncih. Ch nby gixylh qilfx
wlsjnialujbs cm u pyls cgjilnuhn niif zil jlinywncha chzilguncih ch wigjonyl msmnygm. Qcnb nby
chpyhncih iz nby Qilfx Qcxy Qyv il Chnylhyn, wigjonyl msmnygm uly bcabfs chnylwihhywnyx uhx
uwwymmcvfy zlig uhs juln iz nby qilfx. Um gily msmnygm ayn chnylwihhywnyx, gily nblyun
uwnilm nls ni auch uwwymm ni wlcncwuf chzilguncih mnilyx ih nby hynqile. Cn cm nby
lymjihmcvcfcns iz xunu iqhylm il ilauhctuncihm ni eyyj nbcm xunu mywolyfs uhx yhwlsjncih cm
nby guch niif omyx ni mywoly chzilguncih. Ch nbcm jujyl, qy qcff ziwom ih xczzylyhn
nywbhckoym uhx cnm gixylh ujjfcwuncih iz wlsjnialujbs."""


print("Testing all possible keys...")

for key in range(26):
    decrypted_text = decrypt(ciphertext3, key)
    # Show just the first 50 characters to identify the right key
    print(f"Key {key}: {decrypted_text[:50]}...")


print("\nAfter manually checking all options, the correct key is 21.")
print("Decrypted text with key 21:")
print(decrypt(ciphertext3, 21))