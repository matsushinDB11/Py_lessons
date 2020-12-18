# 小数点以下を2進数に変換する
# 引数 f: 変換したい1未満の少数 浮動小数点型
# 引数 i: 少数第i位まで変換する 整数型
# 戻り値: 文字列型
def after_decimal_point_to_bin(f, i):
    bin_array = []
    loop_num = 0
    while True:
        f = f * 2
        if f >= 1.0:
            bin_array.append(1)
            if f == 1.0:
                break
            f -= 1.0
        else:
            bin_array.append(0)

        loop_num += 1
        if loop_num >= i:
            break
    # print(bin_array)
    str_bin = ""
    for i in bin_array:
        str_bin += str(i)
    # print(str_bin)
    return str_bin


# 少数を2進数に変換する
# 引数 f: 変換したい少数 浮動小数点型
# 引数 i: 少数第i位まで変換する
# 戻り値: 浮動小数点型
def double_to_bin(f, i):
    str_f = str(f)
    # 小数点の前後で切り分け
    before_after_decimal_point = str_f.split('.')
    # 整数部を2進数に変換
    bin_before_decimal_point = format(int(before_after_decimal_point[0]), 'b')
    # 小数部の文字列
    after_decimal_point = before_after_decimal_point[1]
    # 0+小数部の文字列
    zero_after_decimal_point = "0." + after_decimal_point
    # 0+小数部 浮動小数点型
    f_zero_after_decimal_point = float(zero_after_decimal_point)
    # print(f_zero_after_decimal_point) 
    # 小数部の2進数 文字列
    str_bin_after_decimal_point = after_decimal_point_to_bin(f_zero_after_decimal_point, i)
    # 整数部の2進数 文字列
    str_bin_before_decimal_point = str(bin_before_decimal_point)
    # 整数部と小数部を結合
    str_bin = str_bin_before_decimal_point + "." + str_bin_after_decimal_point
    # 文字列を浮動小数点に変換
    f_bin = float(str_bin)
    return f_bin


if __name__ == "__main__":
    # テスト
    test = 20.25356323
    float_bin = double_to_bin(test, 10)
    print(float_bin)
