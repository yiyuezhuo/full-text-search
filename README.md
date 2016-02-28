# full-text-search

## Motivation

I want to found comment in Python package ``statsmodels`` summary method's one attribute,Omnibus. I can't use IDE Andconda to find its 
defination and Windows7 full text search can't work proper.So I write this Script to do this.

## Example

    search(r'C:\Users\yiyuezhuo\Anaconda\Lib\site-packages\statsmodels','Omnibus')
    
You can get the list contain the keyword "Omnibus"

	['/iolib/tests/test_summary_old.py',
	 '/iolib/tests/test_summary_old.pyc',
	 '/regression/linear_model.py',
	 '/regression/quantile_regression.py',
	 '/regression/tests/test_regression.py',
	 '/sandbox/regression/gmm.py',
	 '/stats/stattools.py',
	 '/stats/stattools.pyc']
	 
Perhaps you want to look the context for content filter.

	context_get(r'C:\Users\yiyuezhuo\Anaconda\Lib\site-packages\statsmodels','Omnibus',left=100,right=100)
	
get:

	* * * * * * * * * * * * * * * * * * * * 
	C:\Users\yiyuezhuo\Anaconda\Lib\site-packages\statsmodels/iolib/tests/test_summary_old.py
	* * * * * * * * * * * * * * * * * * * * 
				0.9955   Durbin-Watson:              2.559  |
	| Adjusted R-squared:            0.9925   Omnibus:                   0.7486  |
	| F-statistic:                    330.3   Prob(Omnibus):       
	* * * * * * * * * * * * * * * * * * * * 
	C:\Users\yiyuezhuo\Anaconda\Lib\site-packages\statsmodels/iolib/tests/test_summary_old.pyc
	* * * * * * * * * * * * * * * * * * * * 
				0.9955   Durbin-Watson:              2.559  |
	| Adjusted R-squared:            0.9925   Omnibus:                   0.7486  |
	| F-statistic:                    330.3   Prob(Omnibus):       
	* * * * * * * * * * * * * * * * * * * * 
	C:\Users\yiyuezhuo\Anaconda\Lib\site-packages\statsmodels/regression/linear_model.py
	* * * * * * * * * * * * * * * * * * * * 
						('BIC:', ["%#8.4g" % self.bic])
						 ]

			diagn_left = [('Omnibus:', ["%#6.3f" % omni]),
						  ('Prob(Omnibus):', ["%#6.3f" % omnipv]),
		  
	* * * * * * * * * * * * * * * * * * * * 
	C:\Users\yiyuezhuo\Anaconda\Lib\site-packages\statsmodels/regression/quantile_regression.py
	* * * * * * * * * * * * * * * * * * * * 
				   ('Df Model:', None) #[self.df_model])
						]

			diagn_left = [('Omnibus:', ["%#6.3f" % omni]),
						  ('Prob(Omnibus):', ["%#6.3f" % omnipv]),
		  
	* * * * * * * * * * * * * * * * * * * * 
	C:\Users\yiyuezhuo\Anaconda\Lib\site-packages\statsmodels/regression/tests/test_regression.py
	* * * * * * * * * * * * * * * * * * * * 
	   &      -5.5e+06 -1.47e+06       \\\\
	\\bottomrule
	\\end{tabular}
	\\begin{tabular}{lclc}
	\\textbf{Omnibus:}       &  0.749 & \\textbf{  Durbin-Watson:     } &    2.559  \\\\
	\\textbf{Prob(Omnibus):}
	* * * * * * * * * * * * * * * * * * * * 
	C:\Users\yiyuezhuo\Anaconda\Lib\site-packages\statsmodels/sandbox/regression/gmm.py
	* * * * * * * * * * * * * * * * * * * * 
					   #('BIC:', ["%#8.4g" % self.bic])
						 ]

			diagn_left = [('Omnibus:', ["%#6.3f" % omni]),
						  ('Prob(Omnibus):', ["%#6.3f" % omnipv]),
		  
	* * * * * * * * * * * * * * * * * * * * 
	C:\Users\yiyuezhuo\Anaconda\Lib\site-packages\statsmodels/stats/stattools.py
	* * * * * * * * * * * * * * * * * * * * 
	axis) / np.sum(resids**2, axis=axis)
		return dw


	def omni_normtest(resids, axis=0):
		"""
		Omnibus test for normality

		Parameters
		-----------
		resid : array-like
		axis : int, op
	* * * * * * * * * * * * * * * * * * * * 
	C:\Users\yiyuezhuo\Anaconda\Lib\site-packages\statsmodels/stats/stattools.pyc
	* * * * * * * * * * * * * * * * * * * * 
	