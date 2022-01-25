#!/usr/bin/env python3
import os
if os.name == 'posix':
    os.system("printf '\e[8;15;80t'")    
else:
    os.system('mode con: cols=80 lines=15')

def boot_ticket():
    global dfat
    print(' Welcome to Check-a-Ticket.')
    print('\n Importing libraries...')
    import pandas as pd

    print(' Importing datasets and functions...')
    dfat = pd.read_pickle('KENO//KENO_alltime.pkl')
    dfat = dfat[[ 'drawNumber', 'winningNumbers', 'bonus' ]]
    dfat = dfat.to_dict('series')
    payouts = pd.read_pickle('KENO//KENO_payouts.pkl')

    def check_ticket(game_n, num_l, num_g, game_c, bonus):
        os.system('cls' if os.name == 'nt' else 'clear')
        dfat2 = dfat.copy()
        # Create a new instance of dfat2 that only has required draws
        temp_ind = dfat2['drawNumber'][dfat2['drawNumber'] >= game_n].index
        total_won = 0
        for col in dfat2:
            dfat2[col] = dfat2[col].iloc[temp_ind]
            dfat2[col].reset_index(inplace = True, drop = True)
            dfat2[col] = dfat2[col].head(num_g)
        # Check which numbers hit on which games, and account for bonuses
        if bonus == False:
            hit_count = []        
            for drawn in dfat2['winningNumbers']:
                hit = []
                for picked in num_l:
                    if picked in drawn:
                        hit.append(picked)
                hit_count.append(len(hit))
            # Calculate profits w/out bonus
            for L_ind,hits in enumerate(hit_count):
                total_won += (payouts.loc[len(num_l), str(hits)]) * (game_c)
            total_spent = (game_c * num_g)
            total_won = total_won - total_spent
            ticket_value = total_spent + total_won
            if total_won < 0:
                dol_total_won = str(("%.2f" % total_won)).replace('-','-$')
            else:
                dol_total_won = '$'+str(("%.2f" % total_won))
        else:
            hit_count = []
            bonus_count = []
            for indx,drawn in enumerate(dfat2['winningNumbers']):
                hit = []
                for picked in num_l:
                    if picked in drawn:
                        hit.append(picked)
                hit_count.append(len(hit))
                bonus_count.append(int(dfat2['bonus'].iloc[indx]))
            # Calculate profits w/ bonus
            for L_ind,hits in enumerate(hit_count):
                total_won += (payouts.loc[len(num_l), str(hits)]) * (bonus_count[L_ind]) * (game_c)
            total_spent = ((game_c * 2) * num_g)
            total_won = total_won - total_spent
            ticket_value = total_spent + total_won
            if total_won < 0:
                dol_total_won = str(("%.2f" % total_won)).replace('-','-$')
            else:
                dol_total_won = '$'+str(("%.2f" % total_won))
        # Returned information
        if num_g > len(dfat2['drawNumber']):
            remaining_games = int(num_g - len(dfat2['drawNumber']))
            print('\n\n\n The total profit in the first', str(len(dfat2['winningNumbers'])), 'of', str(num_g), 'games was: ', dol_total_won)
            print(' Ticket Value:  $' + ("%.2f" % ticket_value))
            print('\n There are', str(remaining_games), 'games remaining.\n Good Luck! :)')
            res_app = input('\n Hit enter to start again. Enter 1 to reboot application: ')
            os.system('cls' if os.name == 'nt' else 'clear')
            if res_app == '1':
                return boot_ticket()
            else:
                return req_ticket()
        else:
            print('\n\n\n All draws for the ticket have completed! \n The total profit made on the ticket was: ', dol_total_won)
            print(' Ticket Value:  $' + ("%.2f" % ticket_value))
            res_app = input('\n Hit enter to start again. Enter 1 to reboot application: ')
            os.system('cls' if os.name == 'nt' else 'clear')
            if res_app == '1':
                return boot_ticket()
            else:
                return req_ticket()
    # Request ticket information
    def req_ticket():
        num_l = []
        loop_bool = True
        while loop_bool == True:
            os.system('cls' if os.name == 'nt' else 'clear')
            if len(num_l) > 0:
                print('\n\n Previous draw number:', dfat['drawNumber'].iloc[-1], '\n ', num_l)
            else:
                print('\n\n Previous draw number:', dfat['drawNumber'].iloc[-1], '\n ')
            chnum = input(' Please enter your chosen numbers. Enter nothing if done.: ')
            if chnum != '':
                try:
                    chnum = int(chnum)
                except:
                    input(' You did not enter a recognized value. Press Enter to try again.')
                    continue
            if (chnum in range(1,81)) & (chnum not in num_l):
                num_l.append(chnum)
                continue
            elif (chnum in range(1,81)) & (chnum not in num_l):
                input(' You already entered that number. Try a new number,\n or hit enter if done.')
                continue
            elif chnum == '':            
                loop_bool = False
                continue
            else:
                input(' You did not enter a recognized value. Needs to be a number 1-80.\n Press Enter to try again.')
                continue
        # Check number of game    
        def check_num_g():
            global num_g
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n\n Previous draw number:', dfat['drawNumber'].iloc[-1], '\n Chosen numbers:', num_l)
            num_g = input(' How many games did you play?: ')
            num_g = int(num_g)
        def c_n_g():
            try:
                check_num_g()
            except:
                input(' Did not enter a number. Press Enter to try again.')
                return c_n_g()
        c_n_g()    
        # Check starting game number 
        def check_game_n():
            global game_n
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n\n Previous draw number:', dfat['drawNumber'].iloc[-1], '\n Chosen numbers:', num_l)
            print(' Number of games:', num_g)
            game_n = input(' What\'s the starting draw number for your draws?: ')
            game_n = int(game_n)
            if game_n not in list(dfat['drawNumber']):
                input(' Draw number "'+ str(game_n) + '" does not exist. Press Enter to try again.\n')
                return c_g_n()
        def c_g_n():
            try:
                check_game_n()
            except:
                input(' Did not enter a number. Press Enter to try again.')
                return c_g_n()
        c_g_n()    
        # Check whether or not bonus was played
        def check_bonus():
            global bonus
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n\n Previous draw number:', dfat['drawNumber'].iloc[-1], '\n Chosen numbers:', num_l)
            print(' Number of games:', num_g)
            print(' Starting draw number:', game_n)
            check_bonus = input(' Did you play the bonus? (y/n): ')
            check_bonus = check_bonus.lower()
            if (check_bonus == 'y') or (check_bonus == 'yes') or (check_bonus == '1'):
                bonus = True
            elif (check_bonus == 'n') or (check_bonus == 'no') or (check_bonus == '0'):
                bonus = False
            else:
                raise ValueError(' Incorrect entry. Needs one of: "y"/"yes"/"1" or "n"/"no"/"0". Try again.')
        def c_b():
            try:
                check_bonus()
            except:
                input(' You made an incorrect entry. Press Enter to try again')
                return c_b()
        c_b()    
        # Check cost per game
        def check_game_c():
            global game_c
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n\n Previous draw number:', dfat['drawNumber'].iloc[-1], '\n Chosen numbers:', num_l)
            print(' Number of games:', num_g)
            print(' Starting draw number:', game_n)
            print(' Bonus:', 'Yes' if bonus == True else 'No')
            game_c = input(' Cost per game? (not including bonus): ')
            game_c = int(game_c)
        def c_g_c():
            try:
                check_game_c()
            except:
                input(' Did not enter a number. Press Enter to try again.')
                return c_g_c()
        c_g_c()
        return check_ticket(game_n, num_l, num_g, game_c, bonus)

    def init_rt():
        try:
            req_ticket()
        except:
            input(' Something went wrong. Hit enter to retry.')
            return init_rt()

    init_rt()

boot_ticket()