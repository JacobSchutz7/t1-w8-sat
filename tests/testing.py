def test_success_code():
	assert 10 / 2 == 5

def test_testing_failure_code():
	assert 10 / 2 == 3

def text_exception():
	if True:
		raise ValueError("You got a value error!")