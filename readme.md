# In your face! The biased judgement of fear-anger expressions in violence offenders.

Martin Wegrzyn, Sina Westphal & Johanna Kissler,
in preparation

### Abstract


Why is it that certain violent criminals repeatedly find themselves engaged in brawls? Many inmates report having felt provoked or threatened by their victims, which might be due to a tendency to ascribe malicious intentions when faced with ambiguous social signals, termed hostile attribution bias.
The present study presented morphed fear-anger faces to prison inmates with a history of violent crimes, to inmates who sexually abused minors, and to matched controls form the general population. In addition, a test to distinguish basic facial expressions and questionnaires for aggression, psychopathy and personality disorders were administered.
Results show that violent offenders present with a reliable hostile attribution bias, in that they rate ambiguous fear-anger expressions as more angry, compared to both the control population and child molesters. When fitting psychometric functions to the data violent offenders show a lowered threshold to detect anger, as compared to the general population.  This effect is especially pronounced for male faces and correlates with self-reported aggression ratings from questionnaire data. The effects cannot be explained by a general impairment in recognizing expressions, as the violent offenders are as successful in recognizing full-blown basic expressions of emotion as the other groups.
We propose that using an expression identification task and combining it with questionnaire data might aid diagnostics regarding the specificity of the deficit in violent offenders, while providing a reasonable check against potential dissimulation tendencies. Overall, the results indicate that a hostile attribution bias might be one underlying mechanism responsible for acts of physical violence.

### About

This is a repository containing the full data and code of our paper about facial expression recognition in violence offenders (work in progress!).  

### Table of Contents

- the participant data
 - [AFAS](experiment/quest/app/static/logfiles)
 - [PPI-R](experiment/ppi_r.csv)
 - [SCID-II](experiment/scid_ii.csv)
 - [basic expressions and morphed expressions](experiment/data)
- the experiment
  - [AFAS as online questionnaire](experiment/quest)
  - [face recognition experiment](experiment/emoFaces.py)
- the code
  - [Analysis of Questionnaires](notebooks/001_questionnaires.ipynb)
  - [Analysis of basic expressions recognition](notebooks/002_basicExpressions.iypnb)
  - [Importing morph data](notebooks/003_gettingMorphData.iypnb)
  - [Basic analyses of morph data](notebooks/004_basicPlotting.ipynb)
  - [Curve Fitting/Psychophysics](notebooks/005_fittingFunctions.ipynb)

### Requirements

Data analysis was performed with Python 2.7.11 [www.python.org](http://www.python.org) using mainly NumPy, SciPy, Pandas, scikit-learn, Matplotlib, Seaborn and the Jupyter Notebook, all as provided with Anaconda 2.2.5 (Continuum Analytics; [docs.continuum.io/anaconda](http://docs.continuum.io/anaconda)).  
The main experiment was written and rendered with [PsychoPy](http://psychopy.org).  
The AFAS questionnaire was rendered as a html site using [Flask](http://flask.pocoo.org/).  

### Contact

For questions or comments please write to [martin.wegrzyn@uni-bielefeld.de](mailto:martin.wegrzyn@uni-bielefeld.de)
