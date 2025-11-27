# Standard Block Comparison Method

**An auditing framework to break free from "number magic" and measure the true effectiveness of administrative measures.**

## Overview
Huge figures announced by governments and corporations, such as "cumulative total of X people" or "budget of Y billion yen," are often used to obscure the reality (ROI).
This repository provides the "Standard Block Comparison Method," a technique to mathematically determine whether a measure functions as social infrastructure or is merely a statistical "error" by breaking these numbers down to the smallest unit: the "Standard Block" (Basic Municipality).

This method applies the concept of Fermi estimation, using the number of basic municipalities in Japan (approx. 1,700) as a constant to calculate an index (Administrative Density) that allows anyone to intuitively grasp the scale of a project.

## Purpose
*   **DX of Administrative Auditing:** Conducting logical administrative evaluations based on formulas rather than emotions.
*   **Visualization of Scale:** Converting enormous numbers into a "life size" (capacity per municipality) that citizens can actually feel.
*   **Contribution to Civic Tech:** Publishing a universally verifiable evaluation format as open source.

## The Formula

The Effectiveness Impact ($I$) of an administrative measure is defined by the following formula:

$$ I = \frac{V}{B} $$

Here, the Standard Block ($B$) is calculated as follows:

$$ B = \frac{P \times R}{N} $$

### Definitions
*   $P$ (Population): Total population of Japan (approx. 124 million *as of 2023 estimates*)
*   $R$ (Ratio): Ratio of the target attribute (e.g., 1.0 for total population, 0.15 for young adults, etc.)
*   $N$ (Number): Total number of basic municipalities in Japan (approx. 1,718)
*   $V$ (Value): Announced outcome figure (e.g., cumulative 3,000 users, 10 billion yen budget)
*   $B$ (Block): Standard Block (Average target number per municipality)
*   $I$ (Impact): Effectiveness Impact
*   
### Criteria (v2.0)
The calculated Impact value ($I$) represents how many of Japan’s 1,718 municipalities could be fully covered by the measure. Based on this, the "Social Implementation Stage" is judged.

| Impact Value ($I$)     | Estimated Coverage Rate | Verdict           | Benchmark / Meaning |
|------------------------|--------------------------|-------------------|----------------------|
| **$I < 1.0$**          | Less than 0.05%          | **Error Level**   | Out of scope. Cannot even cover one standard municipality. |
| **$1.0 ≤ I < 17$**     | Less than 1%             | **Localized**     | Experimental phase. Not even reaching early adopters. |
| **$17 ≤ I < 172$**     | 1%–10%                   | **Penetration**   | “One per classroom” level. Awareness is beginning to spread. |
| **$172 ≤ I < 859$**    | 10%–50%                  | **Infrastructure**| “One in ten” level. Becoming a foundational public service. |
| **$I ≥ 859$**          | Over 50%                 | **Social OS**     | Majority adoption. A prerequisite for modern society. |

## Case Studies

### 1. Kashiwa City, Chiba Pref.: Preconception Care Project
*   **Link:** [Read full analysis: Kashiwa (JP)](reports/kashiwa_report_2025.md)
*   **Context:** The city introduced apps and services in collaboration with private companies as a "countermeasure against the declining birthrate."
*   **Announced Figure ($V$):** 3,000 users
*   **Target Ratio ($R$):** 0.15 (Assumed women of reproductive age)
*   **Standard Block ($B$):** $124,000,000 \times 0.15 \div 1,718 \approx 10,826$ people
*   **Analysis Result ($I$):** $3,000 \div 10,826 \approx$ **0.27**
*   **Conclusion:** Calculated nationally, this equates to only "0.3 users per municipality." The penetration rate as a policy is at a **"margin of error"** level.

### 2. Osaka-Kansai Expo: Visitor Target
*   **Link:** [Read full analysis: Osaka-Kansai Expo 2025](reports/osaka_expo_analysis_en.md)
*   **Context:** Visitor target for the Expo scheduled for 2025.
*   **Announced Figure ($V$):** 28.2 million people
*   **Target Ratio ($R$):** 1.0 (Total population)
*   **Standard Block ($B$):** $124,000,000 \times 1.0 \div 1,718 \approx 72,176$ people
*   **Analysis Result ($I$):** $28,200,000 \div 72,176 \approx$ **390**
*   **Interpretation:** While this figure gives an Impact of 390, paradoxically it suggests a logistical unreality: "An average of 16,000 people per municipality must be mobilized (including repeats during the period)" to achieve this goal.

## Usage
### 1. Python Script (For Engineers)

You can easily verify numbers at hand using the Python script included in this repository.

### Requirements
*   Python 3.6+

### Execution Commands
```bash
# Example: Verifying headcount (3,000 people, target ratio 100%)
python methodology/block_calculator.py --value 3000 --target_ratio 1.0

# Example: Verifying budget (10 billion yen, target ratio 100%)
python methodology/block_calculator.py --value 10000000000 --target_ratio 1.0
```

### 2. Google Sheets (For Everyone)
You can use this method without coding skills.
Copy the code from `methodology/google_sheets_script.js` into your Google Sheet's "Extensions > Apps Script".

**Formulas:**
*   Calculate Score: `=IMPACT_SCORE(Value, TargetRatio)`
*   Get Verdict: `=IMPACT_VERDICT(Score)`

## Statistical Verification (Monte Carlo Simulation)
This script verifies the robustness of the analysis against arguments such as "Is the target ratio estimate accurate?" or "Is there measurement error?".
It performs tens of thousands of simulations considering parameter uncertainty to calculate confidence intervals.

### Requirements
*   Python 3.6+
*   **NumPy** library

### Execution

1. Install the library
```bash
pip install numpy
```

2. Run the simulation
```bash
# Basic verification (Example: 3,000 users, ratio 0.15)
python verification/sensitivity_analysis.py --value 3000 --target_ratio 0.15

# Advanced settings (Assuming higher uncertainty)
# Use -sd to specify the standard deviation (default is 0.03)
python verification/sensitivity_analysis.py --value 28200000 --target_ratio 1.0 --ratio_sd 0.1
```

### Interpretation
If the lower bound of the "95% Confidence Interval (95% CI)" is below 1.0, you can statistically conclude that the measure is at an "Error Level" even when accounting for uncertainty.

## Extension Module: Budget Portfolio Analysis

## Overview
This module applies the "Standard Block Comparison Method" to all items in a financial statement to visualize the balance between **"Invested Tax (Budget)"** and **"Achieved Outcome (Coverage)."**
This quantifies how **"distorted"** a specific project is in terms of its return to citizens.

## 1. Definition of Budget Impact ($I_{budget}$)
Measures the "weight" of a project's budget relative to the financial scale of a standard municipality (1 Block).

$$ B_{money} = \frac{S_{total}}{N} $$
$$ I_{budget} = \frac{v_{cost}}{B_{money}} $$

*   **$S_{total}$:** **Estimated General Account Budget of a Standard Municipality (Pop. approx. 70k) $\approx$ 30 Billion JPY (approx. $200M USD)**
    *   *Note: We use a fixed "standard wallet size" as the denominator to measure "how huge the spending is relative to the wallet."*
*   **$N$:** Total number of basic municipalities (1,718).
*   **$v_{cost}$:** Settlement amount of the project (e.g., Tablets: 1.5 Billion JPY).
*   **$B_{money}$:** **Standard Budget Block** (Average cost a municipality should spend on a sector).
*   **$I_{budget}$:** **Budget Impact** (How many times the spending is compared to the standard sense of money).

## 2. Definition of Budget Distortion Index ($D_{index}$)
Calculates the degree of "spending money but reaching few people."
A higher value indicates a high probability of **"Poor Cost-Performance"** (e.g., Middleman exploitation, White elephant projects, Vested interests).

$$ D_{index} = \frac{I_{budget}}{I_{coverage}} $$

*   **$I_{budget}$:** Budget Impact (Size of Money)
*   **$I_{coverage}$:** Coverage Impact (Size of Reach *calculated via Standard Block Method*)
*   **$D_{index}$:** **Budget Distortion Index**

---

## The Matrix

By plotting the calculated $I_{budget}$ (Money) and $I_{coverage}$ (People), projects can be classified into four quadrants.

| Quadrant | Status | Verdict ($D_{index}$) | Examples |
| :--- | :--- | :--- | :--- |
| **Q1**<br>(High Money / High Reach) | **Infrastructure** | $D \approx 1$ | Waste collection, Roads, School lunches.<br>Expensive but used by everyone. Appropriate. |
| **Q2**<br>(Low Money / High Reach) | **Innovation** | $D \ll 1$ | Excellent DX policies, SNS PR.<br>Low budget reaching many citizens. "God-tier Projects." |
| **Q3**<br>(Low Money / Low Reach) | **Nominal** | $D \approx 1$ | Small events, Committees.<br>Harmless but ineffective. |
| **Q4**<br>(High Money / Low Reach) | **【Distortion】** | **$D \gg 1$** | **Redevelopments, Tablets, Unused Apps.**<br>**Huge taxes vanishing into the pockets of a few.** |

> **※ Note on Exceptions (Social Safety Nets)**
> Welfare and life-saving projects (e.g., Livelihood Protection, Emergency Medical Services) structurally fall into Q4 (High Cost / Few Targets). These should be evaluated not as "Waste (Distortion)" but as **"Social Costs."**

---

## Simulation: Kashiwa City Case Study

### Case A: Educational Tablets (1.5 Billion JPY / 50% Utilization)
*   **Budget ($I_b$):** Huge (Assumed several times the standard ICT budget) $\rightarrow$ **10.0**
*   **Coverage ($I_c$):** Only half utilized $\rightarrow$ **0.5**
*   **Distortion ($D$):** $10.0 \div 0.5 =$ **20.0 (Abnormal)**
    *   *Verdict:* "Q4 (Distortion)." Effectiveness is too low for the investment amount.

### Case B: Preconception Care (370 Million JPY / 300 Users)
*   **Budget ($I_b$):** Large relative to scale $\rightarrow$ **2.0**
*   **Coverage ($I_c$):** Error level $\rightarrow$ **0.01**
*   **Distortion ($D$):** $2.0 \div 0.01 =$ **200.0 (Extremely Abnormal)**
    *   *Verdict:* "Q4 (The Void)." Money vanishes, and almost no one benefits.

---

## What This Formula Reveals
By pouring financial statement data into this formula, projects plotted in **"Quadrant 4 (High Money / Low Reach)"** are exposed.
This area represents the **"Pathology needing Audit"** (Vested interests, Thoughtless spending).

## Usage (Python Version)
### Workflow: From Theory to Practice

By combining the tools in this repository, you can perform automated auditing through the following workflow:

1.  **Data Preparation (Create CSV)**
    *   Use `prompts/auditor_prompt.md` to instruct an AI (Gemini/ChatGPT/Claude) to analyze financial statement PDFs and generate an `input.csv` file.
2.  **Execution (Run Analysis)**
    *   Load the generated CSV into the Python script.
    *   Command: `python budget_distortion_analyzer.py input.csv`
3.  **Output (Get Results)**
    *   The **"Distortion Index ($D_{index}$)"** and **"Verdict (Quadrant)"** are automatically calculated based on the theory, listing priority projects for audit.
