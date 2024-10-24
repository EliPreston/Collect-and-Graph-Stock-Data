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


def get_info(date_data, price_data):
    print

    high_dates = []
    high_prices = []
    low_dates = []
    low_prices = []


    for (dl, pl) in zip(date_data, price_data):
        info = get_price_info(dl, pl)

        high_dates.append(info[0])
        high_prices.append(info[1])
        low_dates.append(info[2])
        low_prices.append(info[3])
    
    print(f'Highs: \n{high_dates} \n{high_prices}\n')
    print(f'Lows: \n{low_dates} \n{low_prices}\n')
    

def longest_run_yr(date_data, price_data):

    run_dates = []
    run_prices = []

    curr_run_start = ['', -1]
    curr_run_end = ['', -1]
    prev_price = -1
    run_len = -1
    

    for (curr_dt, curr_pr) in zip(date_data, price_data):

        if run_len == -1:
            curr_run_start[0] = curr_dt
            curr_run_start[1] = curr_pr
            
            curr_run_end[0] = curr_dt
            curr_run_end[1] = curr_pr


        if run_len >= 0 and curr_pr > prev_price:
            curr_run_end[0] = curr_dt
            curr_run_end[1] = curr_pr
            run_len += 1
        
        if curr_pr < prev_price:
            run_len = 0


    return 0


def longest_run_increasing(date_data, price_data):

    for (dl, pl) in zip(date_data, price_data):
        info = longest_run_yr(dl, pl)