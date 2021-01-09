class Locators:


    #FIXME use clases

    # ====== main page =======
    search_input_name = 'text'
    suggest_dropdown_xpath = '//div/ul[@class="mini-suggest__popup-content"]/..'
    search_btn_xpath = '//button[@type="submit"]'

    # ====== results page ======
    # used ancestor because the first elements might be advertising or wiki etc
    results_row_xpath = '//li[@class="serp-item"]//div[@id]/ancestor::li'

    # ====== images page ======
    categories_link_xpath = '//a[@class="Link PopularRequestList-Preview"]'
    # image link in image results
    images_link_xpath = '//a[@class ="serp-item__link"]'
    # directly img in the link
    link_img_xpath = './/img'
    # title of an opened picture
    # openimg_title_xpath = '//div[@class="MMOrganicSnippet-Text"]' FIXME
    # preview for opened image
    preview_bigimg_class = 'MMImage-Preview'
    # tag with link to download for opened image
    link_bigimg_class = 'MMImage-Origin'
    forward_circlebtn_class = 'MediaViewer_theme_fiji-ButtonNext'
    backwards_circlebtn_class = 'MediaViewer_theme_fiji-ButtonPrev'


