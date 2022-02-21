# Massachusetts KENO Suite
<h5>Collection of various python scripts for predicting and checking results of Massachusetts KENO.</h5>

<br><h3>Installation/Requirements:</h3>
After cloning the repository, download and extract the "KENO" folder from [HERE](https://drive.google.com/file/d/1jRfkWU4BCPhi9eZOmE5DHgx2QxaTA82K/view?usp=sharing) to the "MA_KENO_Suite" directory.<br><br>
Version:<br>Majority of the python was written in 3.9.7. The rest was written in 3.8.10 on account of OS switch to Ubuntu 20.04 which uses native 3.8.10. On account of complete compatibility I saw no reason to force 3.9.7 for remaining script.
<br><br>Python Libraries:<br>pandas, numpy, matplotlib, requests

<h6><i>Scripting was designed to run in low end computers as I'm using a gaming rig i built 13-14 years ago (check below for specs). Datasets are split and methods involved in the import involve pd.concat on large number of smaller datasets. Due to low performance issue, much of the code is designed for efficiency, while i admit, due to learning over time, there are parts of the code that can still be patched for better performance.</i></h6>

<br><h3>Python Application: Description.</h3>
<b>run_KENO.py:</b> Main application for checking highest occuring numbers, making predictions by call, making predictions by automatic mode, etc.... All around application.
<br><br><b>quick_KENO.py:</b> Quickly generates top profit original-type predictions for 6,7 and 12 spot games.
<br><br><b>pred_testing.py:</b> Application that takes in all predictions and spits out a complete means dataset, 3 datasets corresponding to the prediction types with all profitable combinations, an option with the ability to check any combinations mean, and an option to check any combinations profit value counts.
<br><br><b>check_KENO.py:</b> Check a KENO ticket
<br><br><b>plot_KENO.py:</b> Very simple application to plot value counts over time in a readable manner. (run in interactive shell like an editor)

<br><h3>Python Application Customizations:</h3>
<b>run_KENO.py</b>
- default previous games: adjust variable <b><i>def_prev_l</b></i> to add/change default previous games used for prediction generation<br>
- default number of spots: adjust variable <b><i>def_spot_l</b></i> to add/change your choice of spot numbers for prediction generation<br>
- prediction dataset size for saving: adjust <b><i>if len(dfpredtr)>=500000:</b></i> to whatever number of entries you prefer it to split prediction datasets into in order to be able to import on your computer. (currently set to 500,000, 3 occurances)

<b>quick_KENO.py</b>
- default prediction options: at the end of the application there are 3 listings of <b><i>draw_pred_2</b></i> that you can adjust for your specific combination selection : <i><b> draw_pred_2(<previous game #>, <# of spots for game>, <"O" prediction type selection>) </i></b>

<b>pred_testing.py</b>
- would recommend adjusting variables <b><i>def_prev_l</b></i> and <b><i>def_spot_l</b></i> to correspond to run_KENO.py or whatever specific predictions you're interested in analyzing
- if using the automatic mode, everytime it saves a prediction dataset it names it "dfpredX" where X is the number that it is in order from 1 to whatever number of datasets you have. (ie: 62 is what is in the KENO folder plus the original dfpred which is the active/changing dataset)<br>Add:<br><i><b>print(' dfX...')<br>
dfX=pd.read_pickle('KENO//dfpredX.pkl')<br>
  dfX.drop(columns=drop_cols, inplace=True)</i></b><br> adjusting the X for the number of the new dataset in the folder you'd like to add to prediction analysis. also must add the dfX to the concat and delete area right below the dataset imports. New datasets should be added between the last dfX and dfpred/dfpredC (currently you'd put new one between df62 and dfpredC)
- if you wish to change what is considered "green" in predictions change the ">=0" to whatever you prefer to consider "green"<br> 3 spots:<br><i><b>if dfprmean.loc[pind,pcol]>=0:<br> if dfprmean.loc[pindX,pcolX]>=0:<br>if dfprmean.loc[pindZ,pcolZ]>=0:</i></b>

<b>plot_KENO.py</b>
- at bottom of script you will see <b><i>tempdf=df.tail(200)</b></i>. all you have to do is adjust the index on the dataframe which has been reduced to a single column of just the drawn numbers. if you want the last X game you can use the "tail()" call otherwise use ".iloc[]" with the proper indexing. it takes in rows first so for example <b><i>tempdf=df.iloc[-200:-100]</b></i> would give you the first 100 games of the last 200 games to put it simply. make sure to name the dataframe with the <b><i> tempdf.name = "" </b></i> as this is what is used to name the saved files which can be located in the PLOTS folder after you run the function. there are many commented out examples of proper syntax.
- currently configured to choose number of highest occuring and plot, and number of lowest occuring and plot. out of the box its designed to do 20 highest and 20 lowest, which if you run will find difficult to read. i recommend 3-5 on both. to change the number of numbers it plots you must change the "20" in <b><i> for WKnum in last_dicE.most_common(20): </b></i> and change the "-20" in <b><i> for LKnum in last_dicE.most_common()[-20:]: </b></i> with the WKnum referencing the most occuring (winning) and the LKnum references the least occuring (losing).
  
<b>check_KENO.py</b>
- when given the option after checking a ticket to update dataset by pressing "1", as opposed to hitting enter to put in a diff ticket, the only way you'll actually update is if u update the dataset via <b> run_KENO.py </b> with either the manual update (option 13) to save (option 15), or if you have the automatic mode running in the background and it has updated the dataset since you last checked a ticket.
  
<br><h3>Prediction Types</h3>
"O": Original prediction types. Based on occurances in general. Regardless to when they fell.
<br><br>"X": Positional prediction types. Based on when the occurances occurred. Splits the 20 drawn numbers into bins based on how many numbers you choose. Then predicts based on occurances in those bins.
<br><br>"Z": Mixed-type Predictions are 4 variations that involve combinations of the other 2 prediction types.
<h6><i>*All prediction types are in some way based on a theory/idea of long term occurance vs. short term luck.</i></h6>

<br><h6>My (low-end) PC Specs:<br>CPU: Intel Core 2 Quad CPU @ 2.4GHz x 4<br>Memory: 7.8 GiB<br>GPU: NVIDIA G92 [GeForce GTS 250] v:a2<br>Motherboard: ASUS Striker Extreme</h6>

<br><h6><b>Date Started Project: 10/25/2021<br>Date First Commit: 01/25/2022</b></h6>
<h6>This project is also being used as a resume portfolio piece. Currently looking to leave the restaurant industry forever. Please send me an email at <i>keehan_close@comcast.net</i> if you're looking for entry level developers. Preference in working in data science, but on account of needing to change professions ASAP, I would love any opportunity in development. On account of a lack of formal degrees or certifications (all self taught via free coursewares) negotiations in regards to salary, would be understandable.</h6>
  
RESUME: [HERE](https://drive.google.com/file/d/1aCtLv2Il3alcRCOEeTAJuKBMHj9rK7ap/view?usp=sharing)
