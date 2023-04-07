def deal_success_probability(income, ldr, ic): # ldr - last deal result, which added manually, ic - initial capital
    
    # Find probability
    income.append(ldr)
    m = [1 if i > 0 else 0 for i in income]
    m = [sum(m[:i + 1]) for i in range(len(m))]
    n = [i[0] + 1 for i in enumerate(m)]
    probability = [round(x / y, 4) for x, y in zip(m, n)][-1]

    # Find net income
    net_income = sum(income)

    # Find ROI
    h = []
    h = list(income)
    h.insert(0, ic) # income with initial capital

    investment = [sum(h[:i + 1]) for i in range(len(h))]
    roi = [round((x / y) * 100, 2) for x, y in zip(income, investment)]
    roi_s = sum(roi)
    roi_av = round(roi_s / len(income), 2)

    print(f"\nCurrent deal success probability: {probability}\n")
    print(f"Net income: {net_income}\n")
    print(f"ROI by each deal: {roi}\n")
    print(f"ROI average: {roi_av}\n")


deal_success = [-107, -521, -107, -126,  352,  -58,  221, 193,  -38,  454, -12, -211, 129, 85, 342]

deal_success_probability(deal_success, 230, 1000)
# deal_success_probability(deal_success, -230, 1000)