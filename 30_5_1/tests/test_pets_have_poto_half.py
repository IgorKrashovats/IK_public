{"payload":{"allShortcutsEnabled":false,"fileTree":{"tests":{"items":[{"name":"__pycache__","path":"tests/__pycache__","contentType":"directory"},{"name":"__init__.py","path":"tests/__init__.py","contentType":"file"},{"name":"test_all_pets_are_present.py","path":"tests/test_all_pets_are_present.py","contentType":"file"},{"name":"test_all_pets_have_different_names.py","path":"tests/test_all_pets_have_different_names.py","contentType":"file"},{"name":"test_all_pets_have_name_age_breed.py","path":"tests/test_all_pets_have_name_age_breed.py","contentType":"file"},{"name":"test_pet_friends.py","path":"tests/test_pet_friends.py","contentType":"file"},{"name":"test_pets_have_poto_half.py","path":"tests/test_pets_have_poto_half.py","contentType":"file"},{"name":"test_there_are_no_duplicate_pets_in_the_list.py","path":"tests/test_there_are_no_duplicate_pets_in_the_list.py","contentType":"file"}],"totalCount":8},"":{"items":[{"name":"tests","path":"tests","contentType":"directory"},{"name":"README.md","path":"README.md","contentType":"file"},{"name":"conftest.py","path":"conftest.py","contentType":"file"},{"name":"settings.py","path":"settings.py","contentType":"file"},{"name":"test_pet_frends.py","path":"test_pet_frends.py","contentType":"file"}],"totalCount":5}},"fileTreeProcessingTime":2.616351,"foldersToFetch":[],"repo":{"id":694123115,"defaultBranch":"master","name":"30","ownerLogin":"NikNat223","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2023-09-20T11:27:56.000Z","ownerAvatar":"https://avatars.githubusercontent.com/u/133656990?v=4","public":true,"private":false,"isOrgOwned":false},"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"master","listCacheKey":"v0:1695209367.0","canEdit":false,"refType":"branch","currentOid":"207068e336f22de969d1723f09c57917e44980d9"},"path":"tests/test_pets_have_poto_half.py","currentUser":null,"blob":{"rawLines":["#30.3.1 Написать тест, который проверяет, что на странице со списком питомцев пользователя:\r","# пункт 2: Хотя бы у половины питомцев есть фото.\r","\r","import pytest\r","from selenium.webdriver.support import expected_conditions as EC\r","from selenium.webdriver.support.ui import WebDriverWait\r","from selenium.webdriver.common.by import By\r","\r","\r","def test_half_pets_have_poto(test_show_my_pets):\r","    \"\"\"Поверка того, что на странице \"Мои питомцы\" хотя бы у половины питомцев есть фото\"\"\"\r","\r","    # Установка явного ожидания\r","    element = WebDriverWait(pytest.driver, 10).until(\r","        EC.presence_of_element_located((By.CSS_SELECTOR, '.\\\\.col-sm-4.left')))\r","\r","    # Сохранение элементов статистики в переменную \"statistic\"\r","    statistic = pytest.driver.find_elements(By.CSS_SELECTOR, '.\\\\.col-sm-4.left')\r","\r","    # Сохранение элементов с атрибутом \"img\" в переменную \"images\"\r","    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')\r","\r","    # Получение количества питомцев из данных статистики\r","    number = statistic[0].text.split('\\n')\r","    number = number[1].split(' ')\r","    number = int(number[1])\r","\r","    # Нахождение половины от количества питомцев\r","    half = number // 2\r","\r","    # Нахождение количества питомцев с фотографией\r","    number_of_photos = 0\r","    for i in range(len(images)):\r","        if images[i].get_attribute('src') != '':\r","            number_of_photos += 1\r","\r","    # Проверка того, что количество питомцев с фотографией больше или равно половине количества питомцев\r","    assert number_of_photos >= half\r","    print(f'Количество фото: {number_of_photos}')\r","    print(f'Половина от числа питомцев: {half}')"],"stylingDirectives":[[{"start":0,"end":92,"cssClass":"pl-c"}],[{"start":0,"end":50,"cssClass":"pl-c"}],[],[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":13,"cssClass":"pl-s1"}],[{"start":0,"end":4,"cssClass":"pl-k"},{"start":5,"end":13,"cssClass":"pl-s1"},{"start":14,"end":23,"cssClass":"pl-s1"},{"start":24,"end":31,"cssClass":"pl-s1"},{"start":32,"end":38,"cssClass":"pl-k"},{"start":39,"end":58,"cssClass":"pl-s1"},{"start":59,"end":61,"cssClass":"pl-k"},{"start":62,"end":64,"cssClass":"pl-v"}],[{"start":0,"end":4,"cssClass":"pl-k"},{"start":5,"end":13,"cssClass":"pl-s1"},{"start":14,"end":23,"cssClass":"pl-s1"},{"start":24,"end":31,"cssClass":"pl-s1"},{"start":32,"end":34,"cssClass":"pl-s1"},{"start":35,"end":41,"cssClass":"pl-k"},{"start":42,"end":55,"cssClass":"pl-v"}],[{"start":0,"end":4,"cssClass":"pl-k"},{"start":5,"end":13,"cssClass":"pl-s1"},{"start":14,"end":23,"cssClass":"pl-s1"},{"start":24,"end":30,"cssClass":"pl-s1"},{"start":31,"end":33,"cssClass":"pl-s1"},{"start":34,"end":40,"cssClass":"pl-k"},{"start":41,"end":43,"cssClass":"pl-v"}],[],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":28,"cssClass":"pl-en"},{"start":29,"end":46,"cssClass":"pl-s1"}],[{"start":4,"end":91,"cssClass":"pl-s"}],[],[{"start":4,"end":32,"cssClass":"pl-c"}],[{"start":4,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":27,"cssClass":"pl-v"},{"start":28,"end":34,"cssClass":"pl-s1"},{"start":35,"end":41,"cssClass":"pl-s1"},{"start":43,"end":45,"cssClass":"pl-c1"},{"start":47,"end":52,"cssClass":"pl-en"}],[{"start":8,"end":10,"cssClass":"pl-v"},{"start":11,"end":38,"cssClass":"pl-en"},{"start":40,"end":42,"cssClass":"pl-v"},{"start":43,"end":55,"cssClass":"pl-v"},{"start":57,"end":76,"cssClass":"pl-s"},{"start":59,"end":61,"cssClass":"pl-cce"}],[],[{"start":4,"end":63,"cssClass":"pl-c"}],[{"start":4,"end":13,"cssClass":"pl-s1"},{"start":14,"end":15,"cssClass":"pl-c1"},{"start":16,"end":22,"cssClass":"pl-s1"},{"start":23,"end":29,"cssClass":"pl-s1"},{"start":30,"end":43,"cssClass":"pl-en"},{"start":44,"end":46,"cssClass":"pl-v"},{"start":47,"end":59,"cssClass":"pl-v"},{"start":61,"end":80,"cssClass":"pl-s"},{"start":63,"end":65,"cssClass":"pl-cce"}],[],[{"start":4,"end":67,"cssClass":"pl-c"}],[{"start":4,"end":10,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":13,"end":19,"cssClass":"pl-s1"},{"start":20,"end":26,"cssClass":"pl-s1"},{"start":27,"end":40,"cssClass":"pl-en"},{"start":41,"end":43,"cssClass":"pl-v"},{"start":44,"end":56,"cssClass":"pl-v"},{"start":58,"end":82,"cssClass":"pl-s"}],[],[{"start":4,"end":57,"cssClass":"pl-c"}],[{"start":4,"end":10,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":13,"end":22,"cssClass":"pl-s1"},{"start":23,"end":24,"cssClass":"pl-c1"},{"start":26,"end":30,"cssClass":"pl-s1"},{"start":31,"end":36,"cssClass":"pl-en"},{"start":37,"end":41,"cssClass":"pl-s"},{"start":38,"end":40,"cssClass":"pl-cce"}],[{"start":4,"end":10,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":13,"end":19,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":23,"end":28,"cssClass":"pl-en"},{"start":29,"end":32,"cssClass":"pl-s"}],[{"start":4,"end":10,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":13,"end":16,"cssClass":"pl-en"},{"start":17,"end":23,"cssClass":"pl-s1"},{"start":24,"end":25,"cssClass":"pl-c1"}],[],[{"start":4,"end":49,"cssClass":"pl-c"}],[{"start":4,"end":8,"cssClass":"pl-s1"},{"start":9,"end":10,"cssClass":"pl-c1"},{"start":11,"end":17,"cssClass":"pl-s1"},{"start":18,"end":20,"cssClass":"pl-c1"},{"start":21,"end":22,"cssClass":"pl-c1"}],[],[{"start":4,"end":51,"cssClass":"pl-c"}],[{"start":4,"end":20,"cssClass":"pl-s1"},{"start":21,"end":22,"cssClass":"pl-c1"},{"start":23,"end":24,"cssClass":"pl-c1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":9,"cssClass":"pl-s1"},{"start":10,"end":12,"cssClass":"pl-c1"},{"start":13,"end":18,"cssClass":"pl-en"},{"start":19,"end":22,"cssClass":"pl-en"},{"start":23,"end":29,"cssClass":"pl-s1"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-s1"},{"start":21,"end":34,"cssClass":"pl-en"},{"start":35,"end":40,"cssClass":"pl-s"},{"start":42,"end":44,"cssClass":"pl-c1"},{"start":45,"end":47,"cssClass":"pl-s"}],[{"start":12,"end":28,"cssClass":"pl-s1"},{"start":29,"end":31,"cssClass":"pl-c1"},{"start":32,"end":33,"cssClass":"pl-c1"}],[],[{"start":4,"end":105,"cssClass":"pl-c"}],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":11,"end":27,"cssClass":"pl-s1"},{"start":28,"end":30,"cssClass":"pl-c1"},{"start":31,"end":35,"cssClass":"pl-s1"}],[{"start":4,"end":9,"cssClass":"pl-en"},{"start":10,"end":48,"cssClass":"pl-s"},{"start":29,"end":47,"cssClass":"pl-s1"},{"start":29,"end":30,"cssClass":"pl-kos"},{"start":30,"end":46,"cssClass":"pl-s1"},{"start":46,"end":47,"cssClass":"pl-kos"}],[{"start":4,"end":9,"cssClass":"pl-en"},{"start":10,"end":47,"cssClass":"pl-s"},{"start":40,"end":46,"cssClass":"pl-s1"},{"start":40,"end":41,"cssClass":"pl-kos"},{"start":41,"end":45,"cssClass":"pl-s1"},{"start":45,"end":46,"cssClass":"pl-kos"}]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/NikNat223/30/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":null},"displayName":"test_pets_have_poto_half.py","displayUrl":"https://github.com/NikNat223/30/blob/master/tests/test_pets_have_poto_half.py?raw=true","headerInfo":{"blobSize":"2.11 KB","deleteTooltip":"You must be signed in to make or propose changes","editTooltip":"You must be signed in to make or propose changes","deleteInfo":{"deleteTooltip":"You must be signed in to make or propose changes"},"editInfo":{"editTooltip":"You must be signed in to make or propose changes"},"ghDesktopPath":"https://desktop.github.com","isGitLfs":false,"gitLfsPath":null,"onBranch":true,"shortPath":"a40144d","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2FNikNat223%2F30%2Fblob%2Fmaster%2Ftests%2Ftest_pets_have_poto_half.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"40","truncatedSloc":"30"},"mode":"file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"loggedIn":false,"planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/NikNat223/30/blob/master/tests/test_pets_have_poto_half.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","releasePath":"/NikNat223/30/releases/new?marketplace=true","showPublishActionBanner":false},"rawBlobUrl":"https://github.com/NikNat223/30/raw/master/tests/test_pets_have_poto_half.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"symbolsEnabled":true,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"NikNat223","repoName":"30","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timed_out":false,"not_analyzed":false,"symbols":[{"name":"test_half_pets_have_poto","kind":"function","ident_start":443,"ident_end":467,"extent_start":439,"extent_end":2157,"fully_qualified_name":"test_half_pets_have_poto","ident_utf16":{"start":{"line_number":9,"utf16_col":4},"end":{"line_number":9,"utf16_col":28}},"extent_utf16":{"start":{"line_number":9,"utf16_col":0},"end":{"line_number":40,"utf16_col":0}}}]}},"copilotInfo":null,"copilotAccessAllowed":false,"csrf_tokens":{"/NikNat223/30/branches":{"post":"_H6Z5jY5J545lJxmewqqBoiBDi_KlBfGkmYGC8T24eaaYC5hQmUK7KY_SDABKcgXG8DoGt4C5WVedi8WcrN-1A"},"/repos/preferences":{"post":"bDyaAHHXhKnn1d6Vf7BBNE6boKHhTQfXDw__L1KiOOxG-82r4-283V1u6CYkbX92xNIHj_K6Fpxdq0Vaw9gXwA"}}},"title":"30/tests/test_pets_have_poto_half.py at master · NikNat223/30"}