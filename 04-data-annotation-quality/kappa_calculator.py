# kappa_calculator.py
# This script calculates Cohen's Kappa for inter-annotator agreement.
# It uses the exact data from Project 4 (32 items, 30 matches).

def calculate_kappa(observed_agreement, expected_agreement):
    """Calculates Cohen's Kappa given observed and expected agreement rates."""
    # Prevent division by zero if expected agreement is 100%
    if expected_agreement == 1.0:
        return 1.0 if observed_agreement == 1.0 else 0.0
    
    # The Cohen's Kappa formula
    kappa = (observed_agreement - expected_agreement) / (1.0 - expected_agreement)
    return round(kappa, 4)

# --- Data from Project 4 ---
# Total items labelled: 32
# Number of times Annotator 1 and 2 agreed: 30
# Observed agreement (p_o): 30 / 32
# Expected chance agreement (p_e): 284 / 1024 (calculated from the marginal totals in the confusion matrix)

total_items = 32
matches = 30

observed_agreement = matches / total_items
expected_agreement = 284 / 1024 

# Calculate the score
kappa_score = calculate_kappa(observed_agreement, expected_agreement)

# Print the results
print("=== Project 4: Inter-Annotator Agreement ===")
print(f"Total Items: {total_items}")
print(f"Matches: {matches}")
print(f"Observed Agreement (p_o): {observed_agreement:.4f}")
print(f"Expected Agreement (p_e): {expected_agreement:.4f}")
print(f"Cohen's Kappa (k): {kappa_score}")