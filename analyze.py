from datetime import date



def get_price_info(price_data, date_data):

    print(date_data)
    print(price_data)

    info = []
    high = 0
    low = 1000000
    avg = 0
    pr_points = 0
    dt_points = 0

    for (d, p) in zip(price_data, date_data):
        pass








    # curr_year = date.today().year
    # idx = 0
    # yr_total = 0
    # yr_avg_price = 0
    # yr_len = 0

    # for i in price_data:
    #     # print(f'{curr_year}: {i}')

    #     yr_len = len(i)
    #     if yr_len == 0: pass
    #     else:
    #         yr_total = sum([int(point) for point in i])
    #         yr_avg_price = yr_total/yr_len


    #         print(f'{curr_year} Avg: {yr_avg_price}')


    #     idx += 1
    #     curr_year -= 1