def set_charact(name):
    charcater = {
        "name": name,
        "level": 1,
        "hp": 100,
        "items": ["대나무헬리콥터", "빅라이트", "어디로든 문"],
        "skill": ["펀치", "핵펀치", "피하기"]
    }
print("{0}님 반갑습니다. (HP {1}으로 게임을 시작 합니다" format(character["name"], character["hp"]))
return character

def save_game(filename, charact):
    f = open(filename, "w", encoding="utf-8")
    for key in charact:
        print("$s:$s" % (key, charact[key]))
        f.write("$s:$s\n" % (key,charact))