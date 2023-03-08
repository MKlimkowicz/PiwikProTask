import pytest
import requests
import environment


# incorrect type value - different string, integer and boolean
@pytest.fixture(params=["incorrect", 2, True])
def type_value(request):
    return request.param

# incorrect name value - integer, too long name(61 characters), boolean
@pytest.fixture(params=[2, "t" * 61, True])
def name_value(request):
    return request.param

# incorrect url value - empty string, integer, incorrect url format, boolean, list with empty string and correct url, too long url(over 2083 characters)
@pytest.fixture(params=[[""], [2], ["test@test.com"], [True], ["", "http://example.com"], ["t" * 2084]])
def url_value(request):
    return request.param

@pytest.fixture # Request body with incorrect type
def request_body_incorrect_type(type_value):
    return environment.RequestBody(name="test", type=type_value, urls=["http://example.com", "http://example.org"])

@pytest.fixture # Request body with incorrect name
def request_body_incorrect_name(name_value):
    return environment.RequestBody(name=name_value, type="web", urls=["http://example.com", "http://example.org"])

@pytest.fixture # Request body with incorrect name
def request_body_incorrect_url(url_value):
    return environment.RequestBody(name="test1", type="web", urls=url_value)



def test_create_data_negative(request_body_incorrect_type, request_body_incorrect_name, request_body_incorrect_url):
    url = environment.endpoint()
    data = [
        request_body_incorrect_type.to_dict(),
        request_body_incorrect_name.to_dict(),
        request_body_incorrect_url.to_dict(),
    ]
    
    for req_data in data:
        try:
            response = requests.post(url, json=req_data)
            response.raise_for_status()
        
            assert response.status_code == environment.expected_error_response_code
            response_data = response.json()
            assert isinstance(response_data["detail"], list)
            assert isinstance(response_data["detail"][0]["loc"], list)
            assert isinstance(response_data["detail"][0]["msg"], str)
            assert isinstance(response_data["detail"][0]["type"], str)
        except Exception as e:
            pytest.fail(f"Request failed with exception: {e}")