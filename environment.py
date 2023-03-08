# Request Body
class RequestBody:
    def __init__(self, name: str, type: str, urls: str):
        self.name = name
        self.type = type
        self.urls = urls

    def __repr__(self):
        return f"RequestBody(name={self.name}, type={self.type}, urls={self.urls})"

    def __str__(self):
        return f"Name: {self.name}, Type: {self.type}, URLs: {self.urls}"

    def to_dict(self):
        return {"name": self.name, "type": self.type, "urls": self.urls}

# Endpoint 
def endpoint():
    return "https://prk3.ovh/app-task/apps/"

# Expected correct response body
def get_expected_correct_response():
    return  {
       "name": str,
       "type": str,
       "urls": list,
       "id": str,
       "created_at": str
    }

expected_correct_response = get_expected_correct_response


expected_error_response_code = 422 # expected error response code
expected_correct_response_code = 200 # expected correct response code


# that below would be an option if every app type(web,app and sharepoint) would require veryfing possible name inputs

#@pytest.fixture(params=['web', 'mobile', 'sharepoint'])
#def type_value(request):
#    return request.param

#@pytest.fixture(params=['', 't' * 59, 't' * 60])
#def name_value(request):
#    return request.param

