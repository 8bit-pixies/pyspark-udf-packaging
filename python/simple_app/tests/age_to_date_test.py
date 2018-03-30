
from nose.tools import *
import pandas as pd
from numpy import nan


group_cust = pd.DataFrame([{u'BRTH_DATE': 861062400000.0, u'CUST_NUM': u'102755914'},
 {u'BRTH_DATE': 546739200000.0, u'CUST_NUM': u'107068780'},
 {u'BRTH_DATE': -651283200000.0, u'CUST_NUM': u'109503617'},
 {u'BRTH_DATE': -627436800000.0, u'CUST_NUM': u'109932263'},
 {u'BRTH_DATE': 798249600000.0, u'CUST_NUM': u'112593664'},
 {u'BRTH_DATE': 595382400000.0, u'CUST_NUM': u'113928084'},
 {u'BRTH_DATE': -141436800000.0, u'CUST_NUM': u'116604845'},
 {u'BRTH_DATE': -775094400000.0, u'CUST_NUM': u'118137989'},
 {u'BRTH_DATE': 636249600000.0, u'CUST_NUM': u'123845996'},
 {u'BRTH_DATE': -388972800000.0, u'CUST_NUM': u'128278143'},
 {u'BRTH_DATE': 388195200000.0, u'CUST_NUM': u'128682789'},
 {u'BRTH_DATE': 497923200000.0, u'CUST_NUM': u'131176668'},
 {u'BRTH_DATE': 296611200000.0, u'CUST_NUM': u'133154778'},
 {u'BRTH_DATE': 214531200000.0, u'CUST_NUM': u'134702081'},
 {u'BRTH_DATE': 540345600000.0, u'CUST_NUM': u'136001941'},
 {u'BRTH_DATE': 432864000000.0, u'CUST_NUM': u'144702794'},
 {u'BRTH_DATE': nan, u'CUST_NUM': u'146495861'},
 {u'BRTH_DATE': 594172800000.0, u'CUST_NUM': u'146869787'},
 {u'BRTH_DATE': nan, u'CUST_NUM': u'149291184'},
 {u'BRTH_DATE': -945302400000.0, u'CUST_NUM': u'123867'}])
 
def test_collapse_order():
    """
    checks collapse object based on dummy data.
    """
    from feature_generic import AgeToDate
    
    res1 = AgeToDate(round=True).transform(group_cust)
    res2 = AgeToDate(round=False).transform(group_cust)
    assert res1.AGE[0] == 20.0
    assert res2.AGE[0] > 20.0
