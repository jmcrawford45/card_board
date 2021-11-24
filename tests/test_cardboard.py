import card_board

import pkg_resources

def test_card_from_image():
	assert card_board.card_from_image(pkg_resources.resource_filename(__name__, 'dark_magician.jpg')) == 'test'