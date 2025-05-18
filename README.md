# 🏟️ Betting Odds Simulator

This Python script simulates football match predictions based on historical betting odds and evaluates the profitability of those predictions over multiple attempts.

## 📄 Description

The script reads football match betting odds and actual outcomes from a file (`odds.txt`), simulates predictions using a weighted random method based on those odds, and evaluates how accurate and profitable those predictions would be across multiple trials.

## 📂 Input

* `odds.txt`: A text file containing betting odds and actual outcomes for football matches.

  * Lines starting with `#` are treated as comments and ignored.
  * Each line should have at least 7 space-separated values:

    ```
    <Team1> <Team2> <Odds1> <OddsX> <Odds2> <OtherData> <ActualOutcome>
    ```

    * `<Odds1>`: Odds for a home win
    * `<OddsX>`: Odds for a draw
    * `<Odds2>`: Odds for an away win
    * `<ActualOutcome>`: One of `'1'`, `'X'`, or `'2'`

## ⚙️ How It Works

1. **Reads and Filters Data**:

   * Loads the first 20 non-comment lines from `odds.txt`.

2. **Parses Odds and Outcomes**:

   * Extracts betting odds and actual outcomes.

3. **Generates Weighted Predictions**:

   * For each match, creates a weighted list of outcomes (`'1'`, `'X'`, `'2'`) based on odds.
   * Simulates 20 prediction sets by randomly choosing outcomes based on weights.

4. **Evaluates Predictions**:

   * Compares each prediction set to the actual outcomes.
   * Calculates potential payouts as if 100 units were bet on each correct prediction.

5. **Displays Results**:

   * Prints:

     * Earnings per prediction set
     * Total earnings
     * Average earnings

## 📈 Output Example

```plaintext
[320.0, 200.0, 400.0, ...]
8200.0 40000
410.0
```

* First line: Earnings from each of the 20 prediction sets.
* Second line: Total earnings vs total staked (20 games × 100 units × 20 sets).
* Third line: Average earnings per prediction set.

## 🛠️ Requirements

* Python 3
* No external libraries required

## 📝 Notes

* This is a probabilistic simulation and results will vary on each run.
* Intended for educational and experimental purposes; not suitable for actual betting advice.

## 📬 License

Open for use and modification under the MIT License.
