from imgutils.size import get_width, get_height, get_aspect_ratio
from pathlib import Path

CURRENT_DIR = Path(__file__).parent

def test_get_width_should_return_correct_width():
	assert get_width(CURRENT_DIR / "disco-dingo.png") == 1200

def test_get_height_should_return_correct_height():
	assert get_height(CURRENT_DIR / "disco-dingo.png") == 675

def test_get_aspect_ratio_should_return_correct_ratio():
	assert abs(get_aspect_ratio(CURRENT_DIR / "disco-dingo.png") - (1200 / 675)) < 1e-12
