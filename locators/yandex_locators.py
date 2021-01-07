class Locators:

    # ====== main page =======
    search_input_xpath = "//input[@name='text']"
    suggest_dropdown_xpath = '//div/ul[@class="mini-suggest__popup-content"]/..'
    search_btn_xpath = '//button[@type="submit"]'

    # ====== results page ======
    # used ancestor because the first elements might be advertising or wiki etc
    results_row_xpath = '//li[@class="serp-item"]//div[@id]/ancestor::li'

    # ====== images page ======
    categories_link_xpath = '//a[@class="Link PopularRequestList-Preview"]'

