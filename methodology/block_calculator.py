import argparse
import sys

# 定数定義 (日本の統計データに基づく)
# 2023年推計人口など適宜更新可能
DEFAULT_POPULATION = 124_000_000  # 日本の総人口
DEFAULT_MUNICIPALITIES = 1_718    # 基礎自治体数

def calculate_standard_block(population, target_ratio, municipalities):
    """
    標準ブロック（1自治体あたりの平均ターゲット数）を算出する
    """
    return (population * target_ratio) / municipalities

def calculate_impact(value, standard_block):
    """
    実効性インパクト（I）を算出する
    """
    if standard_block == 0:
        return 0
    return value / standard_block

def get_verdict(impact):
    """
    インパクト値に基づいて判定メッセージを返す
    """
    if impact < 1.0:
        return "【誤差レベル】\n   判定: 1自治体すらカバーできていません (社会的インフラとして機能不全)"
    elif impact < 10.0:
        return "【局所的】\n   判定: 一部地域での実験段階、または特定の層にしか届いていません"
    else:
        return "【実効性あり】\n   判定: 一定の普及が見られ、効果検証が可能なフェーズです"

def main():
    parser = argparse.ArgumentParser(
        description='標準ブロック比較法 (Standard Block Comparison Method) 計算ツール'
    )
    
    # 必須引数
    parser.add_argument(
        '--value', '-v',
        type=float,
        required=True,
        help='発表された成果数（例: 利用者数3000人なら 3000、予算1億円なら 100000000）'
    )

    # オプション引数
    parser.add_argument(
        '--target_ratio', '-r',
        type=float,
        default=1.0,
        help='ターゲット属性の比率 (0.0 〜 1.0)。デフォルトは1.0（全人口）'
    )
    
    parser.add_argument(
        '--population', '-p',
        type=int,
        default=DEFAULT_POPULATION,
        help=f'総人口。デフォルトは {DEFAULT_POPULATION:,}'
    )
    
    parser.add_argument(
        '--municipalities', '-m',
        type=int,
        default=DEFAULT_MUNICIPALITIES,
        help=f'基礎自治体数。デフォルトは {DEFAULT_MUNICIPALITIES:,}'
    )

    args = parser.parse_args()

    # 計算実行
    try:
        standard_block = calculate_standard_block(
            args.population, 
            args.target_ratio, 
            args.municipalities
        )
        
        impact = calculate_impact(args.value, standard_block)
        
        # 結果表示
        print("\n=== 標準ブロック比較法 分析結果 ===")
        print(f"1. 入力値 (Value):       {args.value:,.0f}")
        print(f"2. ターゲット比率:       {args.target_ratio * 100:.1f}%")
        print("-" * 30)
        print(f"3. 標準ブロック (B):     {standard_block:,.1f} (1自治体あたりのキャパシティ)")
        print(f"4. 実効性インパクト (I): {impact:.4f}")
        print("-" * 30)
        print(f"結論: {get_verdict(impact)}")
        print("===================================\n")

    except Exception as e:
        print(f"エラーが発生しました: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
