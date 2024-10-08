import requests
import json
import matplotlib.pyplot as plt

from analyze import get_price_info
from colors import color_list
from tickers import symbols_available
from datetime import date
from simple_term_menu import TerminalMenu



def plot_data_all(ticker, prices, dates):

    # print(dates[1][0].split('-')[0])
    # print(dates[-1][0].split('-')[0])

    data_dates = []
    data_prices = []

    for (p, d) in zip(prices, dates):
        data_dates.append(list(reversed(d)))
        data_prices.append(list(reversed(p)))

    data_dates.reverse()
    data_prices.reverse()

    fig, ax = plt.subplots(figsize=(13, 7))
    
    for i in range(0, len(data_dates)):
        if len(data_dates[i]) != 0:
            ax.plot(data_dates[i], data_prices[i], '-o', label=str(data_dates)[i][0][0:4], color=color_list[i], markersize=1, linewidth=0.25)
    

    ax.set_xlabel('Day X')
    ax.set_ylabel('Share Value closing price ($)')
    # ax.legend(range(date.today().year, 2014, -1), loc='upper right')
    
    if data_dates[-1][0]:
        ax.legend(range(int(data_dates[-1][0][0:4]), int(data_dates[0][0][0:4]) - 1, -1), loc='upper right')
    else:
        ax.legend(range(int(data_dates[-2][0][0:4]), int(data_dates[0][0][0:4]) - 1, -1), loc='upper right')

    ax.set_title(f'${ticker}')
    plt.show()



def plot_data_all_stacked(ticker, prices, dates):

    data_dates = []
    data_prices = []

    for (p, d) in zip(prices, dates):
        data_dates.append(list(reversed(d)))
        data_prices.append(list(reversed(p)))


    fig, ax = plt.subplots(figsize=(13, 7))
    
    for i in range(0, len(data_dates)):
        if len(data_dates[i]) != 0:
            ax.plot([i for i in range(len(data_dates[i]))], data_prices[i], '-o', label=str(data_dates)[i][0][0:4], color=color_list[i], markersize=1, linewidth=0.25)
            # ax.plot(data_dates[i], data_prices[i], '-o', label=str(data_dates)[i][0][0:4], color=color_list[i], markersize=1, linewidth=0.25)
    

    ax.set_xlabel('Day X')
    ax.set_ylabel('Share Value closing price ($)')
    # ax.legend(range(date.today().year, 2014, -1), loc='upper right')
    # ax.legend(range(int(data_dates[1][0][0:4]), int(data_dates[-2][0][0:4]) - 1, -1), loc='upper right')
    # ax.legend(range(int(data_dates[1][0][0:4]), int(data_dates[-1][0][0:4]) - 1, -1), loc='upper right')

    if data_dates[0][0]:
        # ax.legend(range(int(data_dates[-1][0][0:4]), int(data_dates[0][0][0:4]) - 1, -1), loc='upper right')
        ax.legend(range(int(data_dates[0][0][0:4]), int(data_dates[-1][0][0:4]) - 1, -1), loc='upper right')
    else:
        ax.legend(range(int(data_dates[1][0][0:4]), int(data_dates[-1][0][0:4]) - 1, -1), loc='upper right')

    
    ax.set_title(f'${ticker}')
    plt.show()

def plot_data_holiday_inverse(ticker, prices, dates):

    data_dates = []
    data_prices = []


    for (p, d) in zip(prices, dates):
        data_dates.append(list(reversed(d)))
        data_prices.append(list(reversed(p)))

    fig, ax = plt.subplots(figsize=(13, 7))
    
    for i in range(0, len(data_dates)):
        if len(data_dates[i]) != 0:
            ax.plot([i for i in range(len(data_dates[i]))], data_prices[i], '-o', label=str(data_dates)[i][0][0:4], color=color_list[i], markersize=1, linewidth=0.25)
    
    ax.set_xlabel('Jan 1st   -->   Sept 30')
    ax.set_ylabel('Share Value closing price ($)')
    # ax.legend(range(date.today().year, 2014, -1), loc='upper right')
    # ax.legend(range(int(data_dates[-2][0][0:4]), int(data_dates[0][0][0:4]) - 1, -1), loc='upper right')
    ax.legend(range(int(data_dates[1][0][0:4]), int(data_dates[-1][0][0:4]) - 1, -1), loc='upper right')

    ax.set_title(f'${ticker}')
    plt.show()

def plot_data_holiday_szns(ticker, prices, dates):
    # holiday_dates = [
    #     '10-01', '10-02', '10-05', '10-06', '10-07', '10-08', '10-09', '10-12', '10-13', '10-14', '10-15', 
    #     '10-16', '10-19', '10-20', '10-21', '10-22', '10-23', '10-26', '10-27', '10-28', '10-29', '10-30', 
    #     '11-02', '11-03', '11-04', '11-05', '11-06', '11-09', '11-10', '11-11', '11-12', '11-13', '11-16', 
    #     '11-17', '11-18', '11-19', '11-20', '11-23', '11-24', '11-25', '11-27', '11-30', '12-01', '12-02', 
    #     '12-03', '12-04', '12-07', '12-08', '12-09', '12-10', '12-11', '12-14', '12-15', '12-16', '12-17', 
    #     '12-18', '12-21', '12-22', '12-23', '12-24', '12-28', '12-29', '12-30', '12-31']

    data_dates = []
    data_prices = []


    for (p, d) in zip(prices, dates):
        data_dates.append(list(reversed(d)))
        data_prices.append(list(reversed(p)))

    # avg_price_increase(data_prices, data_dates)

    fig, ax = plt.subplots(figsize=(13, 7))
    
    for i in range(0, len(data_dates)):
        if len(data_dates[i]) != 0:
            ax.plot([i for i in range(len(data_dates[i]))], data_prices[i], '-o', label=str(data_dates)[i][0][0:4], color=color_list[i], markersize=1, linewidth=0.25)
            # ax.plot(data_dates[i], data_prices[i], '-o', label=str(data_dates)[i][0][0:4], color=colors[i], markersize=2, linewidth=0.5)
    
    ax.set_xlabel('October 1st: 0   -->   December 31st: 63')
    ax.set_ylabel('Share Value closing price ($)')
    # ax.legend(range(date.today().year, 2014, -1), loc='upper right')
    # ax.legend(range(int(data_dates[-2][0][0:4]), int(data_dates[0][0][0:4]) - 1, -1), loc='upper right')
    ax.legend(range(int(data_dates[1][0][0:4]), int(data_dates[-1][0][0:4]) - 1, -1), loc='upper right')

    ax.set_title(f'${ticker}')
    plt.show()



def parse_local_data(ticker):

    f_name = f'data/{ticker}-data-daily.json'
    f_data = open(f_name)
    data = json.load(f_data)

    data_dates_all = []
    data_prices_all = []

    data_dates_holidays = []
    data_prices_holidays = []

    data_dates_regular = []
    data_prices_regular = []


    date_vals_hol = []
    price_vals_hol = []

    date_vals_reg = []
    price_vals_reg = []

    date_vals = []
    price_vals = []


    curr_year = date.today().year

    for day in data['Time Series (Daily)']:
        curr_date = day
        curr_price = float(data['Time Series (Daily)'][day]['4. close'])

        if int(curr_date.split('-')[0]) != curr_year:
            curr_year = int(curr_date.split('-')[0])

            data_dates_holidays.append(date_vals_hol)
            data_prices_holidays.append(price_vals_hol)
            date_vals_hol = []
            price_vals_hol = []

            data_dates_regular.append(date_vals_reg)
            data_prices_regular.append(price_vals_reg)
            date_vals_reg = []
            price_vals_reg = []

            data_dates_all.append(date_vals)
            data_prices_all.append(price_vals)
            date_vals = []
            price_vals = []
        
        else:
            date_vals.append(curr_date)
            price_vals.append(curr_price)

            if int(curr_date.split('-')[1]) > 9:
                    date_vals_hol.append(curr_date)
                    price_vals_hol.append(curr_price)
                
            if int(curr_date.split('-')[1]) < 10:
                date_vals_reg.append(curr_date)
                price_vals_reg.append(curr_price)
    
    data_dates_holidays.append(date_vals_hol)
    data_prices_holidays.append(price_vals_hol)
    data_dates_regular.append(date_vals_reg)
    data_prices_regular.append(price_vals_reg)
    data_dates_all.append(date_vals)
    data_prices_all.append(price_vals)

    f_data.close()


    # get_price_info(data_dates_all, data_prices_all)
    
    menu_options = ['Plot all historical data (one line)', 'Plot all historical data (years stacked)', 'Plot holiday season data (Oct01 - Dec31)', 'Plot all data excluding holiday season']
    terminal_menu = TerminalMenu(menu_options)
    menu_entry_index = terminal_menu.show()

    if menu_entry_index == 0:
        plot_data_all(ticker, data_prices_all, data_dates_all)
    elif menu_entry_index == 1:
        plot_data_all_stacked(ticker, data_prices_all, data_dates_all)
    elif menu_entry_index == 2:
       plot_data_holiday_szns(ticker, data_prices_holidays, data_dates_holidays)
    elif menu_entry_index == 3:
        plot_data_holiday_inverse(ticker, data_prices_regular, data_dates_regular)



if __name__ == '__main__':

    print('Press \'/\' and type in the stock symbol to search, or scroll with the UP/DOWN arrows:')

    terminal_menu = TerminalMenu(symbols_available)
    menu_entry_index = terminal_menu.show()
    parse_local_data(symbols_available[menu_entry_index])




