from __future__ import division

"""
Baseline Calculations
'Actual per lineup wagers will account for volatility, among other things.'
"""

def optimal_wager(my_expected_win_pct, losing_owner_pct, bankroll):
    bet = (losing_owner_pct / 6) * my_expected_win_pct * bankroll
    return bet

def set_fee_optimal_wager(higher_wager, lower_wager, optimal_wager):
    percent_to_allocate_to_lower_wager = (higher_wager - optimal_wager)/(higher_wager - lower_wager)
    return percent_to_allocate_to_lower_wager

def breakeven_winning_percent(number_entered, number_paid, fee, rake):
    pool = number_entered * fee
    payout = pool - (pool*rake)
    b = number_paid * (fee / payout)
    return b
