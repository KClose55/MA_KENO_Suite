# Massachusetts KENO Suite
<h6>Collection of various python scripts used for predicting and checking results for Massachusetts KENO.</h6>

<br>After cloning the repository, download and extract the "KENO" folder from the download link below to the "MA_KENO_Suite" directory.
<br>LINK: https://drive.google.com/file/d/1jRfkWU4BCPhi9eZOmE5DHgx2QxaTA82K/view?usp=sharing

<h3>Requirements:</h3>
Version:<br>Majority of the python was written in 3.9.7. The rest was written in 3.8.5 on account of OS switch to Ubuntu 20.04 which uses native 3.8.5. On account of complete compatibility I saw no reason to force 3.9.7 for remaining script.
<br><br>Python Libraries:<br>pandas, numpy, matplotlib, requests

<h6>Scripting was designed to run in low end computers as I'm using a gaming rig i built 13-14 years ago. Datasets are split and methods involved in the import involve pd.concat on large number of smaller datasets. Due to low performance issue, much of the code is designed for efficiency, while i admit, due to learning over time, there are parts of the code that can still be patched for better performance.</h6>

<br><h3>Python applications:</h3>
<p>"run_KENO.py": Main application for checking highest occuring numbers, making predictions by call, making predictions by automatic mode, etc.... All around application.
<br><br>"quick_KENO.py": quickly generates top profit original-type predictions for 6,7 and 12 spot games.
<br><br>"pred_testing.py": application that takes in all predictions and spits out a complete means dataset and 3 datasets corresponding to the prediction types with all profitable combinations.
<br><br>"check_KENO.py": check a KENO ticket
<br><br>"plot_KENO.py": very simple application to plot value counts over time in a readable manner. (run in interactive shell like an editor)


<br><h3>Prediction Types</h3>
<h6>All prediction types are in some way based on a theory/idea of long term occurance vs. short term luck.</h6>
<p>"O": Original prediction types. Based on occurances in general. Regardless to when they fell.
<br><br>"X": Positional prediction types. Based on when the occurances occurred. Splits the 20 drawn numbers into bins based on how many numbers you choose. Then predicts based on occurances in those bins.
<br><br>"Z": Mixed-type Predictions are 4 variations that involve combinations of the other 2 prediction types.</p>

<br><h6>Date Started Project: 10/25/2021<br>Date First Commit: 01/25/2022</h6>
