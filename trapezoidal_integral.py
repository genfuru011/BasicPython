from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
from math import sin, pi

# パラメータの定義
a = 0  # 積分区間の開始
b = pi / 2  # 積分区間の終了
n = 100  # 分割数
h = (b - a) / n  # 各区間の幅

# 台形積分法の計算
integral = 0.5 * (sin(a) + sin(b))  # 端点の関数値を半分にする
for i in range(1, n):
    # 中間点の関数値を加算する
    integral = integral + sin(a + i * h)

# 最終的に積分値に幅 h を掛ける
integral = integral * h

# 結果の出力
print(integral)