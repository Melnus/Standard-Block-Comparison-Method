import pandas as pd
import argparse
import sys
import os

# config.py をインポートするためのパス設定
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
try:
    import config
except ImportError:
    print("エラー: 'config.py' が見つかりません。", file=sys.stderr)
    sys.exit(1)

def analyze_budget_distortion(file_path, city_population):
    """
    CSVデータを読み込み、予算歪み指数を計算してCSVとコンソールに出力する
    """
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"エラー: ファイルを読み込めませんでした。\n{e}")
        sys.exit(1)

    # 必須カラムのチェック
    required_cols = ['事業名', '決算額', '推定受益者数']
    for col in required_cols:
        if col not in df.columns:
            print(f"エラー: CSVに必須カラム '{col}' がありません。")
            sys.exit(1)

    # --- 計算ロジック (標準ブロック比較法・拡張版) ---
    
    # 1. 自治体の規模係数 (Scale Factor)
    # 例: 柏市(43万人)なら 430000 / 72176 = 6.0倍
    scale_factor = city_population / config.STD_BLOCK_POP

    # 2. 対象自治体における適正予算単位
    local_std_budget = config.STD_BUDGET_UNIT * scale_factor

    # データフレームに計算結果を追加
    results = []
    
    for index, row in df.iterrows():
        budget = row['決算額']
        users = row['推定受益者数']
        
        # A. 予算インパクト (I_budget)
        # その事業が「自治体規模に対してどれだけ金を食っているか」
        i_budget = budget / local_std_budget

        # B. 普及インパクト (I_coverage)
        # その事業が「標準的な1自治体（7.2万人）をどれだけカバーしているか」
        i_coverage = users / config.STD_BLOCK_POP

        # C. 歪み指数 (D_index)
        # D = 金のデカさ / 人の多さ
        # ※0除算回避
        if i_coverage <= 0.0001:
            d_index = 9999.0 # 測定不能なほどの高コスト
        else:
            d_index = i_budget / i_coverage

        # D. 判定 (Verdict)
        if d_index > 50:
            verdict = "🚨 第4象限: 異常な歪み (要監査)"
        elif d_index > 10:
            verdict = "⚠️ 第4象限: 高コスト体質"
        elif d_index < 1:
            verdict = "💎 第2象限: 高効率・優良"
        else:
            verdict = "✅ 第1/3象限: 適正範囲"

        results.append({
            '事業名': row['事業名'],
            '決算額(円)': int(budget),
            '受益者数(人)': int(users),
            '予算Imp': round(i_budget, 2),
            '普及Imp': round(i_coverage, 4),
            '歪み指数(D)': round(d_index, 1),
            '判定': verdict
        })

    # 結果をDataFrame化
    result_df = pd.DataFrame(results)

    # 歪み指数が高い順（ワースト順）にソート
    result_df = result_df.sort_values(by='歪み指数(D)', ascending=False)

    return result_df

if __name__ == "__main__":
    # コマンドライン引数の設定
    parser = argparse.ArgumentParser(description='自治体決算書・予算歪み分析ツール')
    parser.add_argument('csv_file', help='入力CSVファイルパス')
    parser.add_argument('--pop', type=int, default=435000, help='自治体の人口 (デフォルト: 柏市 435,000)')
    
    args = parser.parse_args()

    print(f"\nAnalyzing... (City Population: {args.pop:,})\n")
    print(f"Reference Constants (from config.py):")
    print(f"- Standard Block Pop: {config.STD_BLOCK_POP:,.0f}")
    print(f"- Standard Budget Unit: {config.STD_BUDGET_UNIT:,.0f}\n")
    
    df_result = analyze_budget_distortion(args.csv_file, args.pop)

    # コンソール表示 (上位10件)
    print(df_result[['事業名', '決算額(円)', '歪み指数(D)', '判定']].head(10).to_string(index=False))

    # CSV保存
    output_filename = "distortion_analysis_result.csv"
    df_result.to_csv(output_filename, index=False, encoding='utf-8-sig')
    print(f"\n全データは '{output_filename}' に保存されました。")
