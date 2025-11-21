def stress_tested_yield(
        price,
        weekly_rent,
        vacancy_weeks_base=2,
        council_rates=2000,
        insurance=1200,
        strata=0,
        other_costs=800,
        lvr=0.8,
        base_interest_rate=0.06,
        rent_drop_stress=0.05,
        vacancy_factor_stress=1.5,
        rate_increase_stress=0.02,
        mgmt_pct=0.07,
        maint_pct=0.05
    ):
    deposit = price * (1 - lvr)
    loan = price * lvr

    # Base
    rent_base = weekly_rent * 52 * (1 - vacancy_weeks_base / 52)
    mgmt_base = rent_base * mgmt_pct
    maint_base = rent_base * maint_pct
    interest_base = loan * base_interest_rate
    costs_base = mgmt_base + maint_base + council_rates + insurance + strata + other_costs + interest_base
    net_base = rent_base - costs_base
    yield_base = net_base / deposit

    # Stress
    vacancy_weeks_stress = min(12, vacancy_weeks_base * vacancy_factor_stress)
    rent_stress = weekly_rent * 52 * (1 - rent_drop_stress) * (1 - vacancy_weeks_stress / 52)
    mgmt_stress = rent_stress * mgmt_pct
    maint_stress = rent_stress * maint_pct
    interest_stress = loan * (base_interest_rate + rate_increase_stress)
    costs_stress = mgmt_stress + maint_stress + council_rates + insurance + strata + other_costs + interest_stress
    net_stress = rent_stress - costs_stress
    yield_stress = net_stress / deposit

    return {
        "Base_Net_Annual_Rent": net_base,
        "Base_Net_Yield": round(yield_base,3),
        "Stress_Net_Annual_Rent": net_stress,
        "Stress_Net_Yield": round(yield_stress,3)
    }


