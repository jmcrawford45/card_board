import card_board

import pkg_resources

def test_card_from_image():
	assert 'DARK MAGICIAN' in card_board.card_from_image(pkg_resources.resource_filename(__name__, 'data/dark_magician_header.jpg'))