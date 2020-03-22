import numpy as np
import fetchmaker
from scipy.stats import binom_test
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd

rottweiler_t1= fetchmaker.get_tail_length('rottweiler')
print(np.mean(rottweiler_t1))
print(np.std(rottweiler_t1))

whippet_rescue= fetchmaker.get_is_rescue('whippet')
num_whippet_rescues = np.count_nonzero(whippet_rescue)
num_whippets= np.size(whippet_rescue)
pval = binom_test(num_whippet_rescues, num_whippets, 0.08)
print(pval)

w = fetchmaker.get_weight('whippet')
t = fetchmaker.get_weight('terrier')
p = fetchmaker.get_weight('pitbull')
print(f_oneway(w, t, p).pvalue)

values= np.concatenate([w, t, p])
labels= ['whippet']* len(w) + ['terrier']*len(t) + ['pitbull']* len(p)
print pairwise_tukeyhsd(values, labels, 0.05)
