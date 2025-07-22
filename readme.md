# Aave V2 DeFi Wallet Credit Scoring

This project scores DeFi wallets based on historical usage of Aave V2 using a transparent, rule-based model. Scores range from **0 to 1000**, where:

- **900–1000**: Highly reliable users
- **500–899**: Normal usage patterns
- **<500**: Risky or exploitative behaviors

## Data

We process a JSON file where each record contains a wallet and its chronological list of transactions (`deposit`, `borrow`, `repay`, etc.).

## Feature Engineering

From raw interactions, we extract:
- `repay_ratio`, `liquidation_count`, `borrow_to_deposit_ratio`, `days_active`, etc.
- Flags for bot behavior or missing repayments

## Scoring Model

The scoring model applies penalties for risky behavior such as:
- Low repayment ratio
- Borrowing more than deposited
- Being liquidated
- Short activity windows (bot-like patterns)

## Output

A file `wallet_scores.csv` is generated with two columns:
wallet_address,score
0x123...,850
0xabc...,320



## Future Work

- Train a supervised ML model on labeled data
- Include additional DeFi protocol interactions
- Use graph-based reputation modeling
