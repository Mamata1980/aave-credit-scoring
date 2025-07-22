import json
import csv
from features import extract_features
from model import score_wallet

def main():
    with open('user_transactions.json', 'r') as f:
        data = json.load(f)

    results = []
    for record in data:
        wallet = record["wallet"]
        txs = record["transactions"]
        features = extract_features(txs)
        score = score_wallet(features)
        results.append({"wallet": wallet, "score": score})

    with open('wallet_scores.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["wallet", "score"])
        writer.writeheader()
        writer.writerows(results)

if __name__ == '__main__':
    main()
