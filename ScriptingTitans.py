from collections import Counter
import textwrap
import colorama
colorama.init()

print(colorama.Fore.GREEN +  '''

 /$$$$$$$$ /$$                       /$$$$$$                                           /$$                        
|__  $$__/| $$                      |_  $$_/                                          | $$                        
   | $$   | $$$$$$$   /$$$$$$         | $$   /$$$$$$$  /$$    /$$ /$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$ 
   | $$   | $$__  $$ /$$__  $$        | $$  | $$__  $$|  $$  /$$//$$__  $$ /$$_____/|_  $$_/   /$$__  $$ /$$__  $$
   | $$   | $$  \ $$| $$$$$$$$        | $$  | $$  \ $$ \  $$/$$/| $$$$$$$$|  $$$$$$   | $$    | $$$$$$$$| $$  \__/
   | $$   | $$  | $$| $$_____/        | $$  | $$  | $$  \  $$$/ | $$_____/ \____  $$  | $$ /$$| $$_____/| $$      
   | $$   | $$  | $$|  $$$$$$$       /$$$$$$| $$  | $$   \  $/  |  $$$$$$$ /$$$$$$$/  |  $$$$/|  $$$$$$$| $$      
   |__/   |__/  |__/ \_______/      |______/|__/  |__/    \_/    \_______/|_______/    \___/   \_______/|__/      
                                                                                                                  
''')
print('''
                __  ,  ,    _, ___,_   ___,  _,,_  ___,___,,  ,  _,     ___,___,___,_   ,  , _, 
                '|_) \_/    (_,' | |_) ' |   /  |_)' | ' |  |\ | / _    ' | ' | ' | '|\  |\ |(_, 
                _|_), /`     _)  |'| \  _|_,'\_'|    |  _|_,|'\|'\_|`     |  _|_, |  |-\ |'\| _) 
                '  (_/      '    ' '  `'       `'    ' '    '  `  _|      ' '     '  '  `'  `'   
                                                                '                               
                                                
'''+ colorama.Fore.RESET)

wont = input(colorama.Fore.LIGHTBLUE_EX + f'''
What tools do you use now ?
             
    1.InvestaPlanner - Find your profitable investment opportunities 
    2.PrfCalc - Calculate your profit gane form investment
    3.Xmoney - convert your rupees to another
    4.Guide - How to use.. {colorama.Fore.RESET}
{colorama.Fore.RED}             
NOTICE! ->> InvestaPlanner Only Use USD for Calculations.
        ->> If your Currency is LKR Please Convert to USD via Xmoney  {colorama.Fore.RESET}           
{colorama.Fore.LIGHTBLUE_EX}
Enter number you wont -{colorama.Fore.RESET}''' )

if wont == "1":   
    print(colorama.Fore.YELLOW +'''
  _____                    _        _____  _                             
 |_   _|                  | |      |  __ \| |                            
   | |  _ ____   _____ ___| |_ __ _| |__) | | __ _ _ __  _ __   ___ _ __ 
   | | | '_ \ \ / / _ / __| __/ _` |  ___/| |/ _` | '_ \| '_ \ / _ | '__|
  _| |_| | | \ V |  __\__ | || (_| | |    | | (_| | | | | | | |  __| |   
 |_____|_| |_|\_/ \___|___/\__\__,_|_|    |_|\__,_|_| |_|_| |_|\___|_|   
                                                                         
                                                                         
''')
    a = '''Giving a Loan (Lending Money): 

    This involves lending your money to individuals or organisations in exchange for interest payments. 
    The risk lies in the borrower's ability to repay the loan, potential default, and the impact of inflation on the returns.

    If you decide to lend your money and earn interest, let's assume you lend out 20% of your monthly salary ($20,000). 
    If you receive a 5% annual interest rate, your potential annual profit would be 
    $20,000 * 0.05 = $1,000.



    '''
    # variable a is giving loan

    b = '''Investing in Gold: 

    Investing in physical gold or gold-related assets is often considered a safe haven. 
    Risks include price volatility and the absence of income generation (e.g., dividends or interest).

    nvesting in physical gold typically doesn't generate income, so the potential profit would come 
    from changes in the gold's value. 
    If you allocate 10% of your monthly salary ($10,000) to gold and it appreciates by 10% in a year, y
    our potential profit would be

    $10,000 * 0.10 = $1,000.
    '''
    # variable b is investing in gold

    c = '''Investing in Currency: 

    Currency trading involves buying and selling foreign currencies. It carries risks related to exchange 
    rate fluctuations, geopolitical events, and economic stability.

    Currency trading can be highly volatile. Assuming you allocate 10% of your monthly salary ($10,000) and 
    achieve a 7% annual return, your potential profit would be 

    $10,000 * 0.07 = $700.

    '''
    # variable c is currency

    d = '''Stock Market: 

    Investing in stocks means buying shares of companies. It offers potential for high returns but comes with 
    the risk of market volatility, economic downturns, and company-specific issues

    Stock market returns can vary widely. If you allocate 30% of your monthly salary ($30,000) to stocks
    and expect an average annual return of 8%, your potential profit would be 

    $30,000 * 0.08 = $2,400
    '''
    # variable d is stock market

    e = '''Investing in Crypto: 

    Cryptocurrency investments, like Bitcoin or Ethereum, can yield substantial returns but 
    are highly volatile and subject to regulatory changes and security risks.

    Cryptocurrency returns are highly variable. If you allocate 10% of your monthly salary ($10,000) 
    to cryptocurrencies and achieve an annual return of 15%, your potential profit would be 

    $10,000 * 0.15 = $1,500
    '''
    # variable e is investing in crypto

    f = '''Trading (Short-term Speculation): 

    Trading involves frequent buying and selling of assets to profit from short-term price movements. 
    It can be profitable but is risky due to market uncertainty and transaction costs.

    Trading profits can be unpredictable. If you allocate 10% of your monthly salary ($10,000) to 
    trading and achieve a 12% annual return, your potential profit would be

    $10,000 * 0.12 = $1,200.'''
    # variable f is investing in Tradig

    g = '''Fixed Deposit: 

    This low-risk investment involves depositing a sum of money in a bank or financial institution for a 
    fixed period at a predetermined interest rate. The primary risk is inflation eroding the purchasing power of returns.

    If you invest 5% of your monthly salary ($5,000) in a fixed deposit with a 3% annual interest rate, 
    your potential profit would be 

    $5,000 * 0.03 = $150.
    '''
    # variable g is Fixed Deposit

    h = '''Buy and Hold (Long-term Investing): 

    Holding assets like stocks or real estate for the long term is a lower-risk strategy compared
    to short-term trading. Risks still exist but tend to be lower due to the longer investment horizon.

    Similar to stocks, if you allocate 10% of your monthly salary ($10,000) to long-term investments 
    and expect an 8% annual return, your potential profit would be

    $10,000 * 0.08 = $800.
    '''
    # variable h is buy and hold

    i = '''Hold and Sell (Special Assets): 

    This refers to holding unique or specialized assets like art, collectibles, or rare commodities. 
    Risks depend on the asset's demand and market trends.

    Profit from special assets depends on the asset type and market demand. 
    Assuming a 5% return on your investment of 5% of your monthly salary ($5,000),
    your potential profit would be

    $5,000 * 0.05 = $250.
    '''
    # variable i is hold and sell

    j = '''Rent or Lease (Real Estate): 

Investing in real estate by renting or leasing properties can provide regular income. 
Risks include property value fluctuations, maintenance costs, and tenant issues.

Rental income can vary by location and property type. Let's assume you invest 20% 
of your monthly salary ($20,000) in real estate and earn an annual rental yield of 5%, 
resulting in a potential profit of 

$20,000 * 0.05 = $1,000.
'''
    # variable j is rent/lease

    
    def print_text_in_box(text): # text wrapper
        lines = textwrap.wrap(text, width=100)  # Wrap text to fit within a 40-character width

        max_length = max(len(line) for line in lines)  # Find the maximum line length
        horizontal_line = '+' + '-' * (max_length + 2) + '+'

        print(horizontal_line)
        for line in lines:
            print(f'| {line.ljust(max_length)} |')  # Left-align text within the box
        print(horizontal_line)

    s1 = [a, b, c, d, e, f, g, h]
    s2 = [a, b, c, e, h]
    s4 = [b, h]
    s7 = [a, b, c, d, g, h]
    s8 = [a, b, g, h ]
    s9 = [b,g]
    s10 = [g]
    s11 = [a, f, g]
    s12 =[d, g, ]
    s13 = [a, d, e, g]
    s14 = [b, c, f, h, i]
    s15 = [a, b,g, h, i,]
    s16 = [j]

    # Define investment options in variables a to j
    # ...

    # Define lists of investment plans based on criteria (s1, s2, s4, etc.)
    # ...

    # Initialize an empty list to store the selected investment options
    last_list = []

    # Get the user's salary with error handling
    try:
        salary = int(input("Enter your monthly salary: " + colorama.Fore.RESET))
    except ValueError:
        print(colorama.Fore.YELLOW + "Invalid input. Please enter a valid number.")
        exit()

    # Choose investment plans based on salary
    A_salary_I_list = []
    if salary > 100000:
        A_salary_I_list += s1
    else:
        A_salary_I_list += s2

    last_list += A_salary_I_list

    # Get the percentage of salary allocated for investment with error handling
    while True:
        try:
            percentage = int(input(colorama.Fore.YELLOW + "Enter percentage: " + colorama.Fore.RESET))
            if not 0< percentage <= 100:
                raise ValueError("Percentage should be between 0 and 100.")
            else:
                break  # Break out of the loop if the input is valid
        except ValueError as e:
            print(f"Invalid input: {e}")

    print(f"Valid Percentage: {percentage}")
    # try:
    #     percentage = int(input(colorama.Fore.YELLOW + "Enter the percentage of your salary for investment: " + colorama.Fore.RESET))
    # except ValueError:
    #     print(colorama.Fore.YELLOW + "Invalid input. Please enter a valid number.")
    #     exit()

    # Choose investment plans based on the percentage
    A_percentage_I_list = []
    
    if percentage > 50:
        A_percentage_I_list += s1
    else:
        A_percentage_I_list += s4

    last_list += A_percentage_I_list

    # Get the risk rate from the user with error handling
    while True:
        try:
            risk = int(input(colorama.Fore.YELLOW + "Enter your risk rate (1-5, where 5 is highest risk): " + colorama.Fore.RESET))
            if risk < 1 or risk > 5:
                raise ValueError("Risk rate should be between 1 and 5.")
            else:
                break  # Break out of the loop if the input is valid
        except ValueError as e:
            print(f"Invalid input: {e}")

    print(f"Valid risk rate: {risk}")


    # Choose investment plans based on risk rate
    A_risk_I_list = []
    if risk == 5:
        A_risk_I_list = s1
    elif risk == 4:
        A_risk_I_list = s7
    elif risk == 3:
        A_risk_I_list = s8
    elif risk == 2:
        A_risk_I_list = s9
    else:
        A_risk_I_list = s10

    last_list += A_risk_I_list

    # Get the profit gain time from the user with error handling

    print(colorama.Fore.YELLOW + "<<< What is your profit gain time >>>")
    print(colorama.Fore.YELLOW + '''
                1 = month
                2 = year
                3 = one time
                4 = after 6 months''')

    while True:
        try:
            A_time_I_list = str(input(colorama.Fore.YELLOW + "Enter corresponding number of your profit gain time: " + colorama.Fore.RESET))
            if A_time_I_list not in "1,2,3,4":
                raise ValueError("Input shoul be one of these: 1, 2, 3, 4.")
            else:
                break  # Break out of the loop if the input is valid
        except ValueError as e:
            print(f"Invalid input: {e}")

    print(f"Valid profit gain time: {A_time_I_list}")
        

    last_list += A_time_I_list


    # Take user inputs for assets
    print(colorama.Fore.YELLOW + '''<<< Do you have followings as an asset? >>>
     y = YES
     n = NO
          ''')

    money = input(colorama.Fore.YELLOW +"1.Money? (y or n): " + colorama.Fore.RESET)
    house = input(colorama.Fore.YELLOW + "2.A Rentable Place? (y or n): "+ colorama.Fore.RESET)
    land = input(colorama.Fore.YELLOW + "3.Land? ( y or n): " + colorama.Fore.RESET)

    asset_list = []
    if money == 'y'and house != 'y' and land != 'y' :
        last_list += s1
        
    elif money != "y" and house == 'y' or land == 'y':
        asset_list = s16
    elif money == 'y'and house == 'y' or land == 'y':
        asset_list = s16 + s1
    else:
        print(colorama.Fore.YELLOW + "Invalid input. Please provide valid inputs (yes/no) for money, house, and land.")

    # Knowledge-related code with error handling
    knowledge_related_list = []
    print(colorama.Fore.YELLOW + '''
we want to know about your investing knowledge
          
<<< Enter the corresponding letter of topic that you have knowledge one by one >>>
          
    a = Giving a Loan (Lending Money)
    b = Investing in Gold
    c = Investing in Currency 
    d = Stock Market 
    e = Investing in Crypto 
    f = Trading (Short-term Speculation) 
    g = Fixed Deposit
    h = Buy and Hold (Long-term Investing) 
    i = Hold and Sell (Special Assets)
          
   !...input 'X' to end the current session
   !...input 'restart' to restart the current session for any mistake       
    ''' + colorama.Fore.RESET)

    while True:
        user_input = input(colorama.Fore.YELLOW + "I have knowledge about topic (or end!)-" + colorama.Fore.RESET)
        # user_input = input("knowledge")
        
        if user_input == 'X':
            break
        if user_input == 'restart':
            knowledge_related_list = []  # Clear the list
        elif user_input not in 'a,b,c,d,e,f,g,h,i,':
            print(colorama.Fore.YELLOW + 'Input Invalid!')
        else:
            knowledge_related_list.append(user_input)

    A_knowledge_I_list = []
    if "e" in knowledge_related_list and "f" in knowledge_related_list and "c" in knowledge_related_list and "d" in knowledge_related_list:
        A_knowledge_I_list += s1
    else:
        A_knowledge_I_list += s15

    last_list += A_knowledge_I_list

    # Count the occurrences of investment options in the final list
    print_list = Counter(last_list)

    # Filter and print the investment options that occur 4 or more times
    result = [investment_option for investment_option, count in print_list.items() if count >= 4]
    
    print(colorama.Fore.YELLOW)                                    
    for text in result:
        print_text_in_box(text)

    if j in asset_list:
        text = j
        print_text_in_box(colorama.Fore.YELLOW + text)
    input()    
elif wont == "3":
    print(colorama.Fore.MAGENTA +'''
 __   __                                 
 \ \ / /                                 
  \ V / _ __ ___   ___  _ __   ___ _   _ 
   > < | '_ ` _ \ / _ \| '_ \ / _ | | | |
  / . \| | | | | | (_) | | | |  __| |_| |
 /_/ \_|_| |_| |_|\___/|_| |_|\___|\__, |
                                    __/ |
                                   |___/ 
''')
# Define exchange rates for different currencies
    usd = 320
    gbp = 402
    eur = 345
    jpy = 2
    cny = 44
    aud = 206



    # Check if the user is an admin
    admin = input("\nAre you an Admin? (y or n) - "+ colorama.Fore.RESET)

    if admin == "y":
        password = input(colorama.Fore.MAGENTA + "Please input the password - "+ colorama.Fore.RESET)
        if password == "admin123":
            # Allow the admin to change currency rates
            cu_name = input(colorama.Fore.MAGENTA + "Which currency rate do you want to change? (please input short form) - " + colorama.Fore.RESET)
            rate = int(input(colorama.Fore.MAGENTA + "Enter the new rate - " + colorama.Fore.RESET))
            print(colorama.Fore.MAGENTA)

            if cu_name == "usd":
                usd = rate
            elif cu_name == "gbp":
                gbp = rate
            elif cu_name == "eur":
                eur = rate
            elif cu_name == "jpy":
                jpy = rate
            elif cu_name == "cny":
                cny = rate
            elif cu_name == "aud":
                aud = rate
            else:
                print("Invalid short name")
        else:
            print(colorama.Fore.YELLOW + "\n-----------------------\nYou are not an admin.\n-----------------------" + colorama.Fore.RESET)

    try:
        # Get the amount to convert from the user
        amount = int(input(colorama.Fore.MAGENTA + "What's the amount you have to convert to another ? Rs." + colorama.Fore.RESET))
        
        # Get the desired currency for conversion
        currency = int(input(colorama.Fore.MAGENTA + ''' 
    What currency do you need to convert to?
                                
    1 - US dollar (usd)
    2 - British pound sterling (gbp)
    3 - Euro (eur)
    4 - Japanese yen (jpy)
    5 - Chinese yuan renminbi (cny)
    6 - Australian dollar (aud)
                            
    Please enter the number of the desired currency - '''+ colorama.Fore.RESET))
        
        if currency not in [1, 2, 3, 4, 5, 6]:
            raise ValueError("Invalid currency number.")
        
        print(colorama.Fore.YELLOW + "-----------------------------------------")
        # Convert and display the converted amount
        if currency == 1:
            print('You will get', int((amount / usd)), 'in USD.')
        elif currency == 2:
            print('You will get', int((amount / gbp)), 'in GBP.')
        elif currency == 3:
            print('You will get', int((amount / eur)), 'in EUR.')
        elif currency == 4:
            print('You will get', int((amount / jpy)), 'in JPY.')
        elif currency == 5:
            print('You will get', int((amount / cny)), 'in CNY.')
        elif currency == 6:
            print('You will get', int((amount / aud)), 'in AUD.')
        
        print("-----------------------------------------" + colorama.Fore.RESET)

    # Handle exceptions, such as invalid input
    except ValueError as e:
        print(f"Error: {e}. Please enter valid inputs.")
    input()
elif wont == "2":
    print(colorama.Fore.RED + '''
  _____  _____  ______    _____      _      
 |  __ \|  __ \|  ____|  / ____|    | |     
 | |__) | |__) | |__    | |     __ _| | ___ 
 |  ___/|  _  /|  __|   | |    / _` | |/ __|
 | |    | | \ \| |      | |___| (_| | | (__ 
 |_|    |_|  \_|_|       \_____\__,_|_|\___|
                                            
                                            
''')
    try:
        # Get the user's monthly salary
        salary = int(input("How much is your monthly salary? - " + colorama.Fore.RESET))
        
        # Get the user's monthly expenses
        expenses = int(input(colorama.Fore.RED + "How much are your monthly expenses? - " + colorama.Fore.RESET))
        
        # Get the percentage allocated for the emergency fund
        present = int(input(colorama.Fore.RED + "What percentage of your salary do you allocate for your emergency fund? - " + colorama.Fore.RESET))
        
        # Calculate the emergency fund
        e_fund = (salary * present) // 100
        
        # Calculate the amount available for investment
        investment = salary - (expenses + e_fund)
        if investment < 0:
            print(colorama.Fore.YELLOW + 'YOUR EXPENSES ARE EXEEDING, UNABLE TO INVEST ' + colorama.Fore.RESET)
            input()
            exit()
        else:
            print(colorama.Fore.YELLOW)
            print("------------------------------------")
            print("Your investment amount is", investment)
            print("------------------------------------")
            print(colorama.Fore.RESET)
        # Ask if the user wants to calculate investment profits
        profit_calc = input(colorama.Fore.RED + "Do you want to calculate your investment profit? (y or n) " + colorama.Fore.RESET)
        
        while profit_calc.lower() == "y":
            # Display investment options
            print(colorama.Fore.RED + '''
            Where would you like to invest?
            
            1 - Giving a Loan (Lending Money)
            2 - Investing in Gold
            3 - Investing in Currency
            4 - Stock Market
            5 - Rent or Lease (Real Estate)
            6 - Investing in Crypto
            7 - Trading (Short-term Speculation)
            8 - Fixed Deposit
            9 - Buy and Hold (Long-term Investing)
            10 - Hold and Sell (Special Assets)
            ''')
            
            # Get the user's chosen investment method
            INV_method = int(input("Enter the number of the investment method you choose - " + colorama.Fore.RESET))
            
            # Calculate profits based on the chosen investment method
            if INV_method == 1:
                profit = investment * 0.05
            elif INV_method == 2:
                profit = investment * 0.1
            elif INV_method == 3:
                profit = investment * 0.07
            elif INV_method == 4:
                profit = investment * 0.08
            elif INV_method == 5:
                profit = investment * 0.05
            elif INV_method == 6:
                profit = investment * 0.15
            elif INV_method == 7:
                profit = investment * 0.12
            elif INV_method == 8:
                profit = investment * 0.03
            elif INV_method == 9:
                profit = investment * 0.08
            else:
                profit = investment * 0.05
            
            # Display the calculated profit
            print(colorama.Fore.YELLOW)
            print("------------------------------------")
            print("Your profit is", profit)
            print("------------------------------------")
            print(colorama.Fore.RESET)
            # Ask if the user wants to try another investment method
            profit_calc = input(colorama.Fore.RED + "Do you want to try another investment method? (y or n) "+ colorama.Fore.RESET)

        print( colorama.Fore.RED + colorama.Style.BRIGHT + "\nBest of luck with your investments!")

    # Handle exceptions, such as invalid input
    except ValueError as e:
        print(f"Error: {e}. Please enter valid inputs.")
    input()
elif wont == "4":
#Define the user manual as a multi-line string
    user_manual = f'''

    {colorama.Fore.RED}{colorama.Style.BRIGHT}               $$$ Financial Investment Tool User Manual $$${colorama.Style.RESET_ALL}{colorama.Fore.RESET}

    This tool is designed to help you make informed decisions about your investments based on your financial situation, risk tolerance, and investment knowledge. Follow the instructions below to use the tool effectively:

    {colorama.Fore.YELLOW} Introduction {colorama.Fore.RESET}

    - The tool provides investment recommendations based on your input.
    - You can choose from different investment options and customize your choices based on your preferences.

    {colorama.Fore.YELLOW} Getting Started{colorama.Fore.RESET}

    1. Run the program, and you'll be presented with a menu that lets you choose your desired action:
    - Enter `1` to get investment recommendations.
    - Enter `2` to calculate profit from your investments.
    - Enter `3` to convert your currency to another currency.
    - Enter any other input to exit the program.

    {colorama.Fore.LIGHTGREEN_EX}>>Get Investment Recommendations.{colorama.Fore.RESET}

    {colorama.Fore.YELLOW} Step 1: Financial Information{colorama.Fore.RESET}

    - You will be asked to provide the following financial information:
    - Your monthly salary.
    - Your monthly expenses.
    - The percentage of your salary allocated for your emergency fund.

        
    {colorama.Fore.YELLOW} Step 2: Investment Amount{colorama.Fore.RESET}

    - The tool will calculate the amount available for investment based on your financial information.
    - You will be asked if you want to calculate investment profits. If you choose to do so, you will be guided through various investment options.

    {colorama.Fore.YELLOW} Step 3: Investment Options{colorama.Fore.RESET}

    - You can select from the following investment options:
    1. Giving a Loan (Lending Money)
    2. Investing in Gold
    3. Investing in Currency
    4. Stock Market
    5. Rent or Lease (Real Estate)
    6. Investing in Crypto
    7. Trading (Short-term Speculation)
    8. Fixed Deposit
    9. Buy and Hold (Long-term Investing)
    10. Hold and Sell (Special Assets)
    
    - Each option provides potential profit information based on your investment amount.

    {colorama.Fore.YELLOW} Step 4: Review and Action{colorama.Fore.RESET}

    - The tool will provide you with investment recommendations based on your preferences and risk tolerance.
    - You can choose to explore different investment methods or exit the program.
    {colorama.Fore.BLUE}--------------------------------------------------------------------------{colorama.Fore.RESET}

    {colorama.Fore.LIGHTGREEN_EX}>>Calculate Profit{colorama.Fore.RESET}

    1. Select option `2` to calculate profit from your investments.
    2. You will be asked for your monthly salary and expenses.
    3. You can choose from various investment methods, and the tool will calculate the potential profit based on your selection.
    4. You can try different investment methods and calculate profits accordingly.
    {colorama.Fore.BLUE}--------------------------------------------------------------------------{colorama.Fore.RESET}

    {colorama.Fore.LIGHTGREEN_EX}>>Currency Conversion{colorama.Fore.RESET}

    1. Select option `3` to convert your currency to another currency.
    2. Provide the amount you wish to convert.
    3. Choose the target currency from the available options.
    4. The tool will calculate the converted amount based on the current exchange rates.
    {colorama.Fore.BLUE}--------------------------------------------------------------------------{colorama.Fore.RESET}

    {colorama.Fore.LIGHTGREEN_EX}>>Admin Access (Password-Protected){colorama.Fore.RESET}

    - The tool provides an admin access option, which is password-protected. To access admin features, you need to enter the correct password.
    {colorama.Fore.BLUE}--------------------------------------------------------------------------{colorama.Fore.RESET}

    {colorama.Fore.LIGHTGREEN_EX}>>Exiting the Program{colorama.Fore.RESET}

    - You can exit the program at any time by entering any input other than `1`, `2`, or `3`.'''

    print(user_manual)
else:
    print("invalid input")
input()