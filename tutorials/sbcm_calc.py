def calc_sbcm(budget_yen, users, city_pop):
    """
    SBCM簡易計算機
    budget_yen: 決算額(円)
    users: 利用者数(人)
    city_pop: 自治体人口(人)
    """
    STD_BLOCK = 72176
    STD_BUDGET = 10000000 # 1000万

    # 規模係数
    scale = city_pop / STD_BLOCK
    
    # インパクト計算
    i_budget = budget_yen / (STD_BUDGET * scale)
    i_coverage = users / STD_BLOCK
    
    # 歪み指数 (0除算回避)
    if i_coverage == 0: return float('inf'), "計測不能"
    d_index = i_budget / i_coverage
    
    # 判定
    verdict = "適正"
    if d_index > 10: verdict = "⚠️ 第4象限 (歪み/要監査)"
    if d_index < 1: verdict = "💎 第2象限 (優秀)"
    
    return d_index, verdict

# 実行例: 柏市(43.5万人)で、予算1億・利用者3000人の場合
d, v = calc_sbcm(100000000, 3000, 435000)
print(f"歪み指数: {d:.2f} -> {v}")
