# mode 替换模式选择
#       0 -> 不替换任何非空白字符
#       1 -> 按替换表替换非空白字符
def get_std_text(raw_text: str, mode: int) -> str:
    # 去除换行符
    std_text = raw_text.replace("\n", "")
    if mode == 1:
        # 替换符号
        for (k, v) in replace_tag_map.items():
            std_text = std_text.replace(k, v)
    return std_text


def get_slips(raw_text: str, length: int) -> list[list[str]]:
    chars = [c for c in raw_text]
    slips = [[]] * length
    for i in range(len(chars)):
        c = chars[i]
        slips[i % length] = slips[i % length] + [c]
    max_length = len(slips[0])

    for i in range(length):
        while len(slips[i]) < max_length:
            slips[i] = slips[i] + [block]
    for line in slips:
        line.reverse()
    return slips


def show_slips(slips: list[list[str]]):
    for line in slips:
        for c in line:
            print(c, end=" ")
        print()


# 填充符
block = "□"
# 字体兼容版的填充符，用于解决某些字体下方框小一号的问题
# block = "口"

# 标点符号替换表
replace_tag_map = {
    ",": block,
    ".": block,
    "!": block,
    "?": block,
    "、": block,
    "，": block,
    "。": block,
    "！": block,
    "？": block
}
# 文本
# text = """
# 那琥珀丹凤瞳，美中镶尊，柔中带钢，一瞥乍有千年帝君之庄威，二督又似旭日柔阳之红颜，三察却归若尘世闲游之过客。
# """
text = """
元丰六年十月十二日夜，解衣欲睡，月色入户，欣然起行。
念无与为乐者，遂至承天寺寻张怀民。
怀民亦未寝，相与步于中庭。
庭下如积水空明，水中藻、荇交横，盖竹柏影也。
何夜无月？何处无竹柏？但少闲人如吾两人者耳。
"""
if __name__ == '__main__':
    print("================ 赛博竹简生成器 v1.0.0 by Eur3ka ================")
    print(text)
    print("==>")
    print("simple mode in 7")
    show_slips(get_slips(get_std_text(text, 0), 7))
    print("full mode in 7")
    show_slips(get_slips(get_std_text(text, 1), 7))
