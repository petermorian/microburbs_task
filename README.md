# Microburbs task

This repo contains the python function and decsription of the stress-tested yield function for Question 1

## Stress Tested Yield Function

Investors normally only look at simple gross yields. That hides the real cash impact of vacancy, management fees and rising interest rates.
This function converts those inputs into a clear signal of cashflow strength under both normal and stressed conditions. The stress scenario assumes higher interest rates, lower rent and higher vacancy.

This function produces two metrics for residential investment properties using a pandas DataFrame. It calculates:
- Base Yield. Net annual cashflow divided by investor equity under normal conditions.
- Stress Yield. Same calculation under a simple stress scenario.

These two values show whether a property is likely to be positive or negative cashflow now, and how exposed it is when conditions worsen.

## Function summary
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

## Inputs
- Price of property
- Weekly rent of property
### OPTIONAL: default parameters
- vacancy_weeks_base. Expected annual vacancy under normal conditions. Default 2 weeks.
- council_rates. Annual council rates cost. Default 2000.
- insurance. Annual landlord insurance cost. Default 1200.
- strata. Annual strata fees if applicable. Default 0.
- other_costs. Catch-all annual costs such as water and minor repairs. Default 800.
- lvr. Loan to value ratio. Defines deposit and loan amount. Default 0.8.
- base_interest_rate. Base investment interest rate applied to the loan. Default 0.06.
- rent_drop_stress. Percentage rent reduction in the stress scenario. Default 0.05.
- vacancy_factor_stress. Multiplier applied to base vacancy weeks under stress. Default 1.5.
- rate_increase_stress. Added interest rate for the stress scenario. Default 0.02.
- mgmt_pct. Property management fee as a share of rent. Default 0.07.
- maint_pct. Annual maintenance allowance as a percentage of rent. Default 0.05.

## Outputs
- Base_Net_Annual_Rent: annual rent amount, net of expenses under normal circumstances
- Base_Net_Yield: net rental yield under normal circumstances
- Stress_Net_Annual_Rent: annual rent amount, net of expenses under stress scenario
- Stress_Net_Yield: net rental yield under stress scenario

# Assumptions
- Assumes IO loan

## Potential imporvements to function
- Include additional parameters like property type, property configuration and suburb. Pull the other parameters (vacancy, management fee%, etc.) automatically by referencing other data sources that already have this information.
- Include additional loan paramters like rate type (IO and P&I)..
- Include tax benefits (e.g. expected tax return or tax bill)




