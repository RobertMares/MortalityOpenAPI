import unittest
import requests
class ApiTest(unittest.TestCase):
    
    API_URL = "http://127.0.0.1:5000/mortality/v.1/"
    MORT_STATE = "{}/mortality-state".format(API_URL)
    MORT_STATE_YEAR = "{}/mortality-state-year".format(API_URL)
    MORT_SCHOLAR_YEAR = "{}/mortality-scholarship-year".format(API_URL)
    MORT_SCHOLAR_STATE = "{}/mortality-scholarship-state".format(API_URL)
    MORT_SEX_YEAR = "{}/mortality-sex-year".format(API_URL)
    MORT_SEX_STATE = "{}/mortality-sex-state".format(API_URL)
    MORT_MEDICAL_YEAR = "{}/mortality-medical-year".format(API_URL)
    MORT_AGE_RANGE = "{}/mortality-age-range".format(API_URL)
    MORT_AGE_RANGE_YEAR = "{}/mortality-age-range-year".format(API_URL)
    TOP_MORB = "{}/top-morbidity".format(API_URL)
    TOP_MORB_YEAR = "{}/top-morbidity-year".format(API_URL)
    TOP_MORT_STATES = "{}/top-mortality-states".format(API_URL)
    TOP_MORT_STATES_YEAR = "{}/top-mortality-states-year".format(API_URL)

    #TEST FOR /mortality-state GET FUNCTION
    def test_1_mortality_state(self): 
        id = 10
        r = requests.get("{}?state={}"
            .format(ApiTest.MORT_STATE, id))
        self.assertEqual(r.status_code, 200)
    
    #TEST FOR /mortality-state-year GET FUNCTION
    def test_2_mortality_state_year(self): 
        state = 10
        year = 2012
        r = requests.get("{}?state={}&year={}"
            .format(ApiTest.MORT_STATE, state, year))
        self.assertEqual(r.status_code, 200)

    #TEST FOR /mortality-scholarship-year GET FUNCTION
    def test_3_mortality_scholarship_year(self): 
        scholar = 2
        year = 2012
        r = requests.get("{}?scholarship={}&year={}"
            .format(ApiTest.MORT_STATE, scholar, year))
        self.assertEqual(r.status_code, 200)
    
    #TEST FOR /mortality-scholarship-state GET FUNCTION
    def test_4_mortality_scholarship_state(self): 
        scholar = 2
        state = 10
        r = requests.get("{}?scholarship={}&state={}"
            .format(ApiTest.MORT_STATE, scholar, state))
        self.assertEqual(r.status_code, 200)

    #TEST FOR /mortality-sex-year GET FUNCTION
    def test_5_mortality_sex_year(self): 
        sex = 2
        year = 2012
        r = requests.get("{}?sex={}&year={}"
            .format(ApiTest.MORT_SEX_YEAR, sex, year))
        self.assertEqual(r.status_code, 200)
    
    #TEST FOR /mortality-sex-state GET FUNCTION
    def test_6_mortality_sex_state(self): 
        sex = 2
        state = 10
        r = requests.get("{}?sex={}&state={}"
            .format(ApiTest.MORT_SEX_STATE, sex, state))
        self.assertEqual(r.status_code, 200)

    #TEST FOR /mortality-medical-year GET FUNCTION
    def test_7_mortality_medical_year(self): 
        medical = 2
        year = 10
        r = requests.get("{}?medical={}&year={}"
            .format(ApiTest.MORT_MEDICAL_YEAR, medical, year))
        self.assertEqual(r.status_code, 200)
    
    #TEST FOR /mortality-age-range GET FUNCTION
    def test_8_mortality_age_range(self): 
        age = 2
        r = requests.get("{}?age={}"
            .format(ApiTest.MORT_AGE_RANGE, age))
        self.assertEqual(r.status_code, 200)
    
    #TEST FOR /mortality-age-range-year GET FUNCTION
    def test_9_mortality_age_range_year(self): 
        age = 2
        year = 2012
        r = requests.get("{}?age={}&year={}"
            .format(ApiTest.MORT_AGE_RANGE_YEAR, age, year))
        self.assertEqual(r.status_code, 200)
    
    #TEST FOR /top-morbidity GET FUNCTION
    def test_10_mortality_top_morbidity(self): 
        r = requests.get("{}"
            .format(ApiTest.TOP_MORB))
        self.assertEqual(r.status_code, 200)
    
    #TEST FOR /top-morbidity-year GET FUNCTION
    def test_11_mortality_top_morbidity_year(self): 
        year = 2012
        r = requests.get("{}?year={}"
            .format(ApiTest.TOP_MORB_YEAR, year))
        self.assertEqual(r.status_code, 200)
    
    #TEST FOR /top-mortality-states GET FUNCTION
    def test_12_top_mortality_states(self): 
        r = requests.get("{}"
            .format(ApiTest.TOP_MORT_STATES))
        self.assertEqual(r.status_code, 200)
    
    #TEST FOR /top-mortality-states-year GET FUNCTION
    def test_13_top_mortality_states_year(self): 
        year = 2012
        r = requests.get("{}?year={}"
            .format(ApiTest.TOP_MORT_STATES_YEAR, year))
        self.assertEqual(r.status_code, 200)