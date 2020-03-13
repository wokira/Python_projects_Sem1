#Ira Aggarwal
#2018039
#Section A
#Group 7 


import unittest 
from a1 import weather_response 
from a1 import has_error
from a1 import get_temperature
from a1 import get_humidity
from a1 import get_pressure
from a1 import get_wind 
from a1 import get_sealevel



class testpoint(unittest.TestCase):

	def test_has_error(self):
		self.assertTrue(has_error("453",weather_response("Delhi","2ab136be1543b5789451a5994364c0d3")))
		self.assertTrue(has_error("London", weather_response("Kolkata", "2ab136be1543b5789451a5994364c0d3")))
		self.assertTrue(has_error("Sydney", weather_response("Chandigarh", "2ab136be1543b5789451a5994364c0d3")))
		self.assertTrue(has_error("Rohtak", weather_response("Mumbai", "2ab136be1543b5789451a5994364c0d3")))
		self.assertTrue(has_error("Ludhiana", weather_response("Bathinda", "2ab136be1543b5789451a5994364c0d3")))

	def test_get_temperature(self):
		self.assertAlmostEqual(get_temperature(weather_response("Delhi","2ab136be1543b5789451a5994364c0d3"),1,"03:00:00"),300,delta=5)
		self.assertAlmostEqual(get_temperature(weather_response("Kolkata","2ab136be1543b5789451a5994364c0d3"),2,"06:00:00"),295,delta=5)
		self.assertAlmostEqual(get_temperature(weather_response("Chandigarh","2ab136be1543b5789451a5994364c0d3"),2,"09:00:00"),299,delta=5)
		self.assertAlmostEqual(get_temperature(weather_response("Sydney","2ab136be1543b5789451a5994364c0d3"),3,"12:00:00"),294,delta=5)
		self.assertAlmostEqual(get_temperature(weather_response("Mumbai","2ab136be1543b5789451a5994364c0d3"),2,"18:00:00"),303,delta=5)

	def test_get_humidity(self):
		self.assertAlmostEqual(get_humidity(weather_response("Delhi","2ab136be1543b5789451a5994364c0d3"),1,"03:00:00"),93,delta=5)
		self.assertAlmostEqual(get_humidity(weather_response("Kolkata","2ab136be1543b5789451a5994364c0d3"),1,"06:00:00"),94,delta=5)
		self.assertAlmostEqual(get_humidity(weather_response("Chandigarh","2ab136be1543b5789451a5994364c0d3"),2,"09:00:00"),92.5,delta=5)
		self.assertAlmostEqual(get_humidity(weather_response("Sydney","2ab136be1543b5789451a5994364c0d3"),2,"12:00:00"),76,delta=5)
		self.assertAlmostEqual(get_humidity(weather_response("London","2ab136be1543b5789451a5994364c0d3"),3,"18:00:00"),85,delta=5)

	def test_get_pressure(self):
		self.assertAlmostEqual(get_pressure(weather_response("Rohtak","2ab136be1543b5789451a5994364c0d3"),3,"03:00:00"),994,delta=5)
		self.assertAlmostEqual(get_pressure(weather_response("Delhi","2ab136be1543b5789451a5994364c0d3"),1,"06:00:00"),995,delta=5)

		self.assertAlmostEqual(get_pressure(weather_response("Ludhiana","2ab136be1543b5789451a5994364c0d3"),2,"09:00:00"),994,delta=5)
		self.assertAlmostEqual(get_pressure(weather_response("Mumbai","2ab136be1543b5789451a5994364c0d3"),2,"12:00:00"),1025,delta=5)
		self.assertAlmostEqual(get_pressure(weather_response("Bathinda","2ab136be1543b5789451a5994364c0d3"),3,"18:00:00"),995,delta=5)

	def test_get_wind(self):
		self.assertAlmostEqual(get_wind(weather_response("Delhi","2ab136be1543b5789451a5994364c0d3"),1,"03:00:00"),2.15,delta=5)
		self.assertAlmostEqual(get_wind(weather_response("Rohtak","2ab136be1543b5789451a5994364c0d3"),2,"06:00:00"),1.32,delta=5)
		self.assertAlmostEqual(get_wind(weather_response("Kolkata","2ab136be1543b5789451a5994364c0d3"),3,"09:00:00"),2.00,delta=5)
		self.assertAlmostEqual(get_wind(weather_response("Bathinda","2ab136be1543b5789451a5994364c0d3"),4,"12:00:00"),1.15,delta=5)
		self.assertAlmostEqual(get_wind(weather_response("Mumbai","2ab136be1543b5789451a5994364c0d3"),2,"15:00:00"),2.25,delta=5)

	def test_get_sealevel(self):
		self.assertAlmostEqual(get_sealevel(weather_response("Delhi","2ab136be1543b5789451a5994364c0d3"),2,"03:00:00"),1020,delta=5) 
		self.assertAlmostEqual(get_sealevel(weather_response("Chandigarh","2ab136be1543b5789451a5994364c0d3"),1,"06:00:00"),1020,delta=5) 
		self.assertAlmostEqual(get_sealevel(weather_response("Sydney","2ab136be1543b5789451a5994364c0d3"),2,"09:00:00"),1035,delta=5) 
		self.assertAlmostEqual(get_sealevel(weather_response("Mumbai","2ab136be1543b5789451a5994364c0d3"),2,"03:00:00"),1025,delta=5) 
		self.assertAlmostEqual(get_sealevel(weather_response("Ludhiana","2ab136be1543b5789451a5994364c0d3"),2,"15:00:00"),1018,delta=5) 
		



		

if __name__=='__main__':
	unittest.main()
