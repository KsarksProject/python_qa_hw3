from selene import browser, be, have


def test_search_valid_query(browser_with_custom_size):
    """Тест успешного поиска с валидным запросом."""
    search_input = browser.element('[name="q"]')
    search_input.should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(
        have.text('Tests with Selene can be built either in a simple straightforward "selenide" style')
    )


def test_search_no_results(browser_with_custom_size):
    """Тест поиска с запросом, который не должен давать результатов."""
    search_input = browser.element('[name="q"]')

    # Ввод случайного набора символов
    search_input.should(be.present).clear().type('ssssssssssssssllllllllllllllrrrrrrrsdferwfhfgdhgrrr').press_enter()

    # Проверка на отсутствие результатов
    browser.element('[id="botstuff"]').should(
        have.text('did not match any documents')
    )
