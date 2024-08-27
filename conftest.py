import pytest
from utils.driver_factory import DriverFactory

@pytest.fixture(scope="class")
def setup(request):
    driver = DriverFactory.get_driver()
    request.cls.driver = driver
    yield
    driver.quit()
