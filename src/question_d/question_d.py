#write functions here, don't add input('') statements here!

def get_assessment_value(value):
	"""
	Returns the assessment value, which is 60% of the actual property value.
	Example: value=10000 -> 6000
	"""
	return value * 0.60


def get_tax_assessed(assessment_value):
	"""
	Returns the property tax based on assessment value at $0.72 per $100.
	That is, tax rate = 0.72/100 = 0.0072 of the assessment value.
	Example: assessment_value=6000 -> 43.20
	"""
	return assessment_value * 0.0072
