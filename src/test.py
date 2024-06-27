import pytest
from dash.testing.application_runners import import_app

@pytest.fixture
def dash_duo(dash_duo):
    app = import_app('app')  # Replace 'app' with your app module name
    dash_duo.start_server(app)
    yield dash_duo

def test_header_exists(dash_duo):
    dash_duo.wait_for_element("#header", timeout=10)
    header = dash_duo.find_element("#header")
    assert header is not None
    assert header.text == "Pink Morsel Visualizer"

def test_visualization_exists(dash_duo):
    dash_duo.wait_for_element("#visualization", timeout=10)
    visualization = dash_duo.find_element("#visualization")
    assert visualization is not None

def test_region_picker_exists(dash_duo):
    dash_duo.wait_for_element("#region-picker", timeout=10)
    region_picker = dash_duo.find_element("#region-picker")
    assert region_picker is not None