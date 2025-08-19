# CCDF サンプル

このリポジトリは、**経験的 CCDF (Complementary Cumulative Distribution Function)** と  
**理論的 CCDF (標準正規分布, 平均0・分散1)** を重ねて表示するサンプルです。

![CCDFの例](./ccdf_example.png)

## セットアップ方法

Python 3 系を前提としています。  
まず仮想環境を作成し、必要なライブラリをインストールしてください。

```bash
# 仮想環境の作成
python3 -m venv .venv

# 仮想環境の有効化 (Linux / macOS)
source .venv/bin/activate

# 仮想環境の有効化 (Windows PowerShell)
.venv\Scripts\Activate.ps1

# 必要なライブラリのインストール
pip install numpy matplotlib scipy
```

## 実行方法

```bash
python ccdf_sample.py
```

実行すると、経験的 CCDF と標準正規分布の理論的 CCDF がプロットされます。
（対数スケールでプロットしており、尾部の違いを観察できます。）

## スクリプト概要

* `ccdf_sample.py`
* 平均 0、標準偏差 1 の正規乱数を生成し、経験的 CCDF と理論的 CCDF を重ねて表示します。

## ライセンス

このリポジトリは [MIT License](./LICENSE)のもとで公開されています。