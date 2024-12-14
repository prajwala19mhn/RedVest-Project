import numpy as np

# The given SP500 mock data 
data = [
    {"user_id": "user1", "session_duration": 120, "performance": [0.4, -0.1, 0.8, 0.1, 0.5]},
    {"user_id": "user2", "session_duration": 200, "performance": [0.3, -0.2, 1.0, 0.0, 0.6]},
    {"user_id": "user3", "session_duration": 150, "performance": [0.5, -0.3, 0.9, -0.2, 0.7]}
]
sp500_performance = [0.3, -0.1, 0.8, -0.2, 0.6]  # SP500 Performance (%)

# alpha and beta calculationns
def calculate_alpha_beta(user_perf, sp500_perf):
    user_returns = np.array(user_perf)
    market_returns = np.array(sp500_perf)
    
    beta = np.cov(user_returns, market_returns)[0][1] / np.var(market_returns)
    alpha = np.mean(user_returns) - beta * np.mean(market_returns)
    
    return alpha, beta

# Analysis portion
def analyze_users(data, sp500_performance):
    # top user by session_duration
    top_user = max(data, key=lambda x: x['session_duration'])
    
    # alpha and beta calcs needed for top user
    alpha, beta = calculate_alpha_beta(top_user['performance'], sp500_performance)
    
    # report generation
    print("=== User Activity Report ===")
    print(f"Top User by Activity: {top_user['user_id']} with {top_user['session_duration']} minutes.")
    print(f"Alpha for {top_user['user_id']}: {alpha:.2f}")
    print(f"Beta for {top_user['user_id']}: {beta:.2f}")
    print("===========================")

# Running analysis
if __name__ == "__main__":
    analyze_users(data, sp500_performance)
