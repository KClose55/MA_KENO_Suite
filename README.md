# Massachusetts KENO Suite
<h5>Collection of various python scripts for predicting and checking results of Massachusetts KENO.</h5>

<br><h3>Requirements:</h3>
After cloning the repository, download and extract the "KENO" folder from [HERE](https://drive.google.com/file/d/1jRfkWU4BCPhi9eZOmE5DHgx2QxaTA82K/view?usp=sharing) to the "MA_KENO_Suite" directory.<br><br>
Version:<br>Majority of the python was written in 3.9.7. The rest was written in 3.8.5 on account of OS switch to Ubuntu 20.04 which uses native 3.8.5. On account of complete compatibility I saw no reason to force 3.9.7 for remaining script.
<br><br>Python Libraries:<br>pandas, numpy, matplotlib, requests

<h6><i>Scripting was designed to run in low end computers as I'm using a gaming rig i built 13-14 years ago (check below for specs). Datasets are split and methods involved in the import involve pd.concat on large number of smaller datasets. Due to low performance issue, much of the code is designed for efficiency, while i admit, due to learning over time, there are parts of the code that can still be patched for better performance.</i></h6>

<br><h3>"Python Application": Description.</h3>
"run_KENO.py": Main application for checking highest occuring numbers, making predictions by call, making predictions by automatic mode, etc.... All around application.
<br><br>"quick_KENO.py": Quickly generates top profit original-type predictions for 6,7 and 12 spot games.
<br><br>"pred_testing.py": Application that takes in all predictions and spits out a complete means dataset, 3 datasets corresponding to the prediction types with all profitable combinations, an option with the ability to check any combinations mean, and an option to check any combinations profit value counts.
<br><br>"check_KENO.py": Check a KENO ticket
<br><br>"plot_KENO.py": Very simple application to plot value counts over time in a readable manner. (run in interactive shell like an editor)

<br><h3>Python Application Customizations:</h3>
to be continued tomorrow...

<br><h3>Prediction Types</h3>
"O": Original prediction types. Based on occurances in general. Regardless to when they fell.
<br><br>"X": Positional prediction types. Based on when the occurances occurred. Splits the 20 drawn numbers into bins based on how many numbers you choose. Then predicts based on occurances in those bins.
<br><br>"Z": Mixed-type Predictions are 4 variations that involve combinations of the other 2 prediction types.
<h6><i>*All prediction types are in some way based on a theory/idea of long term occurance vs. short term luck.</i></h6>

<br><h6><b>Date Started Project: 10/25/2021<br>Date First Commit: 01/25/2022</b></h6>

<br><h6>My (low-end) PC Specs:<br>CPU: Intel Core 2 Quad CPU @ 2.4GHz x 4<br>Memory: 7.8 GiB<br>GPU: NVIDIA G92 [GeForce GTS 250] v:a2<br>Motherboard: ASUS Striker Extreme</h6>
