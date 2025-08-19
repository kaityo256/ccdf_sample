import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm


# 平均average、標準偏差sigmaのデータをN個生成
# 実際のデータの代わり
def make_data(N, average, sigma):
    return np.random.normal(loc=average, scale=sigma, size=N)


# データを平均0、分散1に正規化し、そのCCDF(Complementary Cumulative Distribution Function, 補累積分布関数)を返す。
# x座標とy座標を返す
def get_normalized_ccdf(data):
    average = np.average(data)
    sigma = np.std(data)
    data = (data - average) / sigma
    sorted_data = np.sort(data)
    ccdf = 1.0 - np.arange(1, len(sorted_data) + 1) / len(sorted_data)
    return sorted_data, ccdf


def main():
    N = 1000  # データ数
    sigma = 2.0  # 標準偏差
    average = 10.0  # 平均
    # データの生成(実際にはシミュレーションから得る)
    data = make_data(N, average, sigma)

    # データから正規化したCCDFを取得
    x, y = get_normalized_ccdf(data)

    # 平均0、分散1のガウス分布に対応するCCDF(理論値)の計算
    ccdf_theory = norm.sf(x, loc=0, scale=1)
    plt.figure()
    plt.plot(x, y, marker=".", linestyle="none", label="Data")
    plt.plot(
        x,
        ccdf_theory,
        color="red",
        linewidth=2,
        label="Gaussian CCDF (mean=0, var=1)",
    )
    plt.xlabel("x")
    plt.ylabel("CCDF(x)")
    plt.yscale("log")  # べき分布などを見る場合は log スケールにすることが多い
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
