/**
 * ==========================================
 * Standard Block Comparison Method for Google Sheets (v2.0)
 * 標準ブロック比較法 カスタム関数スクリプト
 * ==========================================
 * 
 * 【導入方法 / How to Install】
 * 1. Googleスプレッドシートを開く (Open Google Sheets)
 * 2. メニューの「拡張機能」>「Apps Script」をクリック (Extensions > Apps Script)
 * 3. このコードを貼り付けて保存 (Paste this code and save)
 * 4. シート上で関数として使用可能になります (Use as custom functions)
 */

/**
 * 定数設定
 */
const CONSTANTS = {
  POPULATION: 124000000, // 総人口
  MUNICIPALITIES: 1718   // 基礎自治体数
};

/**
 * 標準ブロック（B）を算出
 * @customfunction
 */
function STANDARD_BLOCK(targetRatio = 1.0) {
  if (typeof targetRatio !== 'number') return "Error: Ratio must be a number";
  return (CONSTANTS.POPULATION * targetRatio) / CONSTANTS.MUNICIPALITIES;
}

/**
 * 実効性インパクト（I）を算出
 * @customfunction
 */
function IMPACT_SCORE(value, targetRatio = 1.0) {
  if (!value) return 0;
  const block = STANDARD_BLOCK(targetRatio);
  return value / block;
}

/**
 * インパクト値から詳細な判定コメントを返す (v2.0)
 * @param {number} score インパクト値
 * @return {string} 判定コメント
 * @customfunction
 */
function IMPACT_VERDICT(score) {
  if (score === "") return "";
  
  if (score < 1.0) {
    return "💀 誤差レベル (Error Level)";
  } else if (score < 14.0) {
    return "⚠️ 局所的 (Localized / 郵便局以下)";
  } else if (score < 32.0) {
    return "🏠 基礎インフラ級 (Infrastructure / 郵便局超え)";
  } else if (score < 700.0) {
    return "🏪 コンビニ級 (Convenience / コンビニ超え)";
  } else if (score < 7000.0) {
    return "🚀 普及フェーズ (Penetration / 人口1%超え)";
  } else {
    return "👑 社会OS級 (Social OS / 人口10%超え)";
  }
}
