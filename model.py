def score_wallet(features: dict) -> int:
    score = 1000

    if features['repay_ratio'] < 0.25:
        score -= 300
    elif features['repay_ratio'] < 0.75:
        score -= 150

    if features['liquidation_count'] > 0:
        score -= 200

    if features['borrow_to_deposit_ratio'] > 1:
        score -= 200

    if features['days_active'] < 2:
        score -= 100

    if features['bot_behavior_flag']:
        score -= 150

    score = max(0, min(1000, score))  # Clamp
    return score
