from datetime import date




def get_price_info(date_data, price_data):

    # info = []
    high_pr = 0
    high_dt = ''
    low_pr = 1000000
    low_dt = ''

    avg = 0
    pr_points = 0
    pr_sum = 0
    dt_points = 0


    for (dt, pr) in zip(date_data, price_data):

        pr_points += 1
        pr_sum += pr
        dt_points += 1
        
        if pr > high_pr:
            high_pr = pr
            high_dt = dt            
        if pr < low_pr:
            low_pr = pr
            low_dt = dt

    avg = pr_sum / pr_points

    print(f'Data Points: {pr_points} \nHigh: {high_pr} - {high_dt} \nLow: {low_pr} - {low_dt} \nAvg: {avg} \nHigh - Low: {high_pr - low_pr} \n')
    
    return (high_dt, high_pr, low_dt, low_pr, avg, pr_sum, pr_points)


def get_info(price_data, date_data):

    high_dates = []
    high_prices = []
    low_dates = []
    low_prices = []


    for (dl, pl) in zip(price_data, date_data):
        info = get_price_info(dl, pl)

        high_dates.append(info[0])
        high_prices.append(info[1])
        low_dates.append(info[2])
        low_prices.append(info[3])
    
    print(f'Highs: \n{high_dates} \n{high_prices}\n')
    print(f'Lows: \n{low_dates} \n{low_prices}\n')
    
