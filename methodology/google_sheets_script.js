/**
 * 標準ブロック比較法 (Standard Block Comparison Method) for Google Sheets
 * 
 * 使い方:
 * 1. スプレッドシートのメニューから [拡張機能] > [Apps Script] を開く
 * 2. このコードを貼り付けて保存する
 * 3. シート上で関数として使用する
 *    例: =IMPACT_SCORE(3000, 0.15)
 */

const CONSTANTS = {
  POPULATION: 124000000, // 日本の総人口 (2023)
  MUNICIPALITIES: 1718   // 基礎自治体数
};

/**
 * 標準ブロック（1自治体あたりのキャパシティ）を計算
 * @param {number} targetRatio ターゲット比率 (0.0 - 1.0)
 * @return {number} 標準ブロック数
 */
function STANDARD_BLOCK(targetRatio = 1.0) {
  if (targetRatio <= 0 || targetRatio > 1) throw new Error("比率は0〜1の間で指定してください");
  return (CONSTANTS.POPULATION * targetRatio) / CONSTANTS.MUNICIPALITIES;
}

/**
 * 実効性インパクト(I)を計算
 * @param {number} value 発表された成果数（人数や金額）
 * @param {number} targetRatio ターゲット比率 (デフォルト1.0)
 * @return {number} インパクト値
 * @customfunction
 */
function IMPACT_SCORE(value, targetRatio = 1.0) {
  const block = STANDARD_BLOCK(targetRatio);
  return value / block;
}

/**
 * インパクト値から判定コメントを返す
 * @param {number} impact インパクト値
 * @return {string} 判定コメント
 * @customfunction
 */
function IMPACT_VERDICT(impact) {
  if (impact < 1.0) return "💀 誤差レベル (1自治体未満)";
  if (impact < 17.2) return "⚠️ 局所的 (普及率1%未満)";
  if (impact < 172.0) return "🚀 普及フェーズ (普及率1%〜10%)";
  if (impact < 859.0) return "🏠 基礎インフラ (普及率10%〜50%)";
  return "👑 社会OS (普及率50%以上)";
}
