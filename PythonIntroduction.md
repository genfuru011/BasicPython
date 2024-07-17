# 【確認課題】PYTHON 入門 

## 問 1. 計算

提出ファイル：`QUADRATIC_FORMULA.PY`

2 次方程式 $AX^2+BX+C=0$ の解 $X$ は、下式で求めることができます:

$X = \DFRAC{-B\PM \SQRT{B^2 - 4AC}}{2A}$

この解の公式を実装して、次の 2 次方程式の解が得られるかを確認しましょう。

(1) $X^2-6X+9=0$ の解は $3$  
(2) $X^2+2X-8=0$ の解は $2$ と $-4$  
(3) $8X^2-6X-35=0$ の解は $5/2$ と $-7/4$  
(4) $X^2+1=0$ の解は $J$ と $-J$ &NBSP; ( $J$ は虚数単位)

<!-- (X-3)^2 -->
<!-- (X-2)(X+4) -->
<!-- (2X-5)(4X+7) -->
<!-- (X+J)(X-J) -->

### 補足

- ルート（ $\SQRT{A}$ ）は、2 分の 1 乗（ $A^{1/2}$ ）として計算できます。
- (4) の解には計算誤差が含まれると思います。PYTHON がどこまで正しい精度で計算できるかは『[制御構文 問 4. マシンイプシロン][EPS]』を解くと分かります。（お楽しみに）

[EPS]: HTTPS://SHINONOME.IO/PYTHONTUTORIALFORDSCOURSE/EXERCISE/02_02_BASICS_OF_PYTHON_CONTROL.HTML#ID5

---

## 問 2. 文字列

提出ファイル：`PI.PY`

`HOW I WANT A DRINK, ALCOHOLIC` の英単語の文字数を並べると 314159 になり、円周率の数字の並びと同じになります。

この問題で実装するのは、24 単語からなる下の英文:

```
HOW I WANT A DRINK, ALCOHOLIC OF COURSE, AFTER THE HEAVY CHAPTERS INVOLVING
QUANTUM MECHANICS. ALL OF THY GEOMETRY, HERR PLANCK, IS FAIRLY HARD.
```

の文字数を並べた文字列 (STR 型) を出力するプログラムです。
実行結果は円周率 24 桁目までの `314159265358979323846264` になるはずです。

### 補足

- 求めるのは「英単語の文字数」なので記号は無視する必要があります。
-  ヒント。下のコードのように `LIST, MAP, LEN` 関数を用いると、与えられたリストの各要素の文字数を得ることができます。
    ```PYTHON
    >>> LIST(MAP(LEN, ["A", "BC", "DEF"]))
    [1, 2, 3]
    ```
    つまり、区切って文字を数えてくっつければ解けそう…？
