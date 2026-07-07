import numpy as np

def generate_signal(history):
    if not history or len(history) < 3:
        return {"action": "WAIT", "exit_at": 1.5, "confidence": "LOW", "reason": "Not enough data"}
    arr = np.array(history)
    mean, std = np.mean(arr), np.std(arr)
    last = arr[-1]
    if last <= mean - (std * 0.8):
        return {"action": "🟢 FLY / ENTRY", "exit_at": max(round(mean + (std * 0.5), 2), 1.5), "confidence": "HIGH", "reason": f"Drop below avg ({round(mean,2)})."}
    if last >= mean + (std * 1.2):
        return {"action": "🔴 EXIT / CASHOUT", "exit_at": max(round(mean - (std * 0.3), 2), 1.2), "confidence": "HIGH", "reason": f"Spike above avg ({round(mean,2)})."}
    return {"action": "🟡 HOLD / OBSERVE", "exit_at": round(mean, 2), "confidence": "MEDIUM", "reason": "Market stable."}