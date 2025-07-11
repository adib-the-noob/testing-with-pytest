import pytest
import source.shapes as shapes
import math

class TestCircle:

    def setup_method(self, method):
        print(f"Setting up method: {method}")
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        print(f"Setting up method: {method}")

    def test_area(self):
        assert self.circle.area() == math.pi ** self.circle.radius ** 2

    def test_one(self):
        assert True