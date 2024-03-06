{"payload":{"allShortcutsEnabled":false,"fileTree":{"tests":{"items":[{"name":"__pycache__","path":"tests/__pycache__","contentType":"directory"},{"name":"__init__.py","path":"tests/__init__.py","contentType":"file"},{"name":"test_all_pets_are_present.py","path":"tests/test_all_pets_are_present.py","contentType":"file"},{"name":"test_all_pets_have_different_names.py","path":"tests/test_all_pets_have_different_names.py","contentType":"file"},{"name":"test_all_pets_have_name_age_breed.py","path":"tests/test_all_pets_have_name_age_breed.py","contentType":"file"},{"name":"test_pet_friends.py","path":"tests/test_pet_friends.py","contentType":"file"},{"name":"test_pets_have_poto_half.py","path":"tests/test_pets_have_poto_half.py","contentType":"file"},{"name":"test_there_are_no_duplicate_pets_in_the_list.py","path":"tests/test_there_are_no_duplicate_pets_in_the_list.py","contentType":"file"}],"totalCount":8},"":{"items":[{"name":"tests","path":"tests","contentType":"directory"},{"name":"README.md","path":"README.md","contentType":"file"},{"name":"conftest.py","path":"conftest.py","contentType":"file"},{"name":"settings.py","path":"settings.py","contentType":"file"},{"name":"test_pet_frends.py","path":"test_pet_frends.py","contentType":"file"}],"totalCount":5}},"fileTreeProcessingTime":2.520905,"foldersToFetch":[],"repo":{"id":694123115,"defaultBranch":"master","name":"30","ownerLogin":"NikNat223","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2023-09-20T11:27:56.000Z","ownerAvatar":"https://avatars.githubusercontent.com/u/133656990?v=4","public":true,"private":false,"isOrgOwned":false},"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"master","listCacheKey":"v0:1695209367.0","canEdit":false,"refType":"branch","currentOid":"207068e336f22de969d1723f09c57917e44980d9"},"path":"tests/test_all_pets_have_name_age_breed.py","currentUser":null,"blob":{"rawLines":["# 30.3.1 Написать тест, который проверяет, что на странице со списком питомцев пользователя:\r","# пункт 3: У всех питомцев есть имя, возраст и порода.\r","\r","import pytest\r","from selenium.webdriver.support import expected_conditions as EC\r","from selenium.webdriver.support.ui import WebDriverWait\r","from selenium.webdriver.common.by import By\r","\r","\r","def test_there_are_a_name_age_and_gender(test_show_my_pets):\r","    \"\"\"Поверка, что на странице \"Мои питомцы\" у всех питомцев есть имя, возраст и порода\"\"\"\r","\r","    # Установка явного ожидания\r","    element = WebDriverWait(pytest.driver, 10).until(\r","        EC.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))\r","\r","    # Сохранение элементов с данными о питомцах в переменную \"pet_data\"\r","    pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')\r","\r","    # Перебираются данные из переменной \"pet_data\"\r","    # Сохраняются имя, возраст и порода, остальное меняется на пустую строку и разделяется пробелом\r","    # Находится количество элементов в получившемся списке и сравнивается с ожидаемым результатом\r","    for i in range(len(pet_data)):\r","        data_pet = pet_data[i].text.replace('\\n', '').replace('×', '')\r","        split_data_pet = data_pet.split(' ')\r","        result = len(split_data_pet)\r","        assert result == 3"],"stylingDirectives":[[{"start":0,"end":93,"cssClass":"pl-c"}],[{"start":0,"end":55,"cssClass":"pl-c"}],[],[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":13,"cssClass":"pl-s1"}],[{"start":0,"end":4,"cssClass":"pl-k"},{"start":5,"end":13,"cssClass":"pl-s1"},{"start":14,"end":23,"cssClass":"pl-s1"},{"start":24,"end":31,"cssClass":"pl-s1"},{"start":32,"end":38,"cssClass":"pl-k"},{"start":39,"end":58,"cssClass":"pl-s1"},{"start":59,"end":61,"cssClass":"pl-k"},{"start":62,"end":64,"cssClass":"pl-v"}],[{"start":0,"end":4,"cssClass":"pl-k"},{"start":5,"end":13,"cssClass":"pl-s1"},{"start":14,"end":23,"cssClass":"pl-s1"},{"start":24,"end":31,"cssClass":"pl-s1"},{"start":32,"end":34,"cssClass":"pl-s1"},{"start":35,"end":41,"cssClass":"pl-k"},{"start":42,"end":55,"cssClass":"pl-v"}],[{"start":0,"end":4,"cssClass":"pl-k"},{"start":5,"end":13,"cssClass":"pl-s1"},{"start":14,"end":23,"cssClass":"pl-s1"},{"start":24,"end":30,"cssClass":"pl-s1"},{"start":31,"end":33,"cssClass":"pl-s1"},{"start":34,"end":40,"cssClass":"pl-k"},{"start":41,"end":43,"cssClass":"pl-v"}],[],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":40,"cssClass":"pl-en"},{"start":41,"end":58,"cssClass":"pl-s1"}],[{"start":4,"end":91,"cssClass":"pl-s"}],[],[{"start":4,"end":32,"cssClass":"pl-c"}],[{"start":4,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":27,"cssClass":"pl-v"},{"start":28,"end":34,"cssClass":"pl-s1"},{"start":35,"end":41,"cssClass":"pl-s1"},{"start":43,"end":45,"cssClass":"pl-c1"},{"start":47,"end":52,"cssClass":"pl-en"}],[{"start":8,"end":10,"cssClass":"pl-v"},{"start":11,"end":38,"cssClass":"pl-en"},{"start":40,"end":42,"cssClass":"pl-v"},{"start":43,"end":55,"cssClass":"pl-v"},{"start":57,"end":86,"cssClass":"pl-s"}],[],[{"start":4,"end":72,"cssClass":"pl-c"}],[{"start":4,"end":12,"cssClass":"pl-s1"},{"start":13,"end":14,"cssClass":"pl-c1"},{"start":15,"end":21,"cssClass":"pl-s1"},{"start":22,"end":28,"cssClass":"pl-s1"},{"start":29,"end":42,"cssClass":"pl-en"},{"start":43,"end":45,"cssClass":"pl-v"},{"start":46,"end":58,"cssClass":"pl-v"},{"start":60,"end":89,"cssClass":"pl-s"}],[],[{"start":4,"end":51,"cssClass":"pl-c"}],[{"start":4,"end":100,"cssClass":"pl-c"}],[{"start":4,"end":98,"cssClass":"pl-c"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":9,"cssClass":"pl-s1"},{"start":10,"end":12,"cssClass":"pl-c1"},{"start":13,"end":18,"cssClass":"pl-en"},{"start":19,"end":22,"cssClass":"pl-en"},{"start":23,"end":31,"cssClass":"pl-s1"}],[{"start":8,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":27,"cssClass":"pl-s1"},{"start":28,"end":29,"cssClass":"pl-s1"},{"start":31,"end":35,"cssClass":"pl-s1"},{"start":36,"end":43,"cssClass":"pl-en"},{"start":44,"end":48,"cssClass":"pl-s"},{"start":45,"end":47,"cssClass":"pl-cce"},{"start":50,"end":52,"cssClass":"pl-s"},{"start":54,"end":61,"cssClass":"pl-en"},{"start":62,"end":65,"cssClass":"pl-s"},{"start":67,"end":69,"cssClass":"pl-s"}],[{"start":8,"end":22,"cssClass":"pl-s1"},{"start":23,"end":24,"cssClass":"pl-c1"},{"start":25,"end":33,"cssClass":"pl-s1"},{"start":34,"end":39,"cssClass":"pl-en"},{"start":40,"end":43,"cssClass":"pl-s"}],[{"start":8,"end":14,"cssClass":"pl-s1"},{"start":15,"end":16,"cssClass":"pl-c1"},{"start":17,"end":20,"cssClass":"pl-en"},{"start":21,"end":35,"cssClass":"pl-s1"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":21,"cssClass":"pl-s1"},{"start":22,"end":24,"cssClass":"pl-c1"},{"start":25,"end":26,"cssClass":"pl-c1"}]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/NikNat223/30/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":null},"displayName":"test_all_pets_have_name_age_breed.py","displayUrl":"https://github.com/NikNat223/30/blob/master/tests/test_all_pets_have_name_age_breed.py?raw=true","headerInfo":{"blobSize":"1.71 KB","deleteTooltip":"You must be signed in to make or propose changes","editTooltip":"You must be signed in to make or propose changes","deleteInfo":{"deleteTooltip":"You must be signed in to make or propose changes"},"editInfo":{"editTooltip":"You must be signed in to make or propose changes"},"ghDesktopPath":"https://desktop.github.com","isGitLfs":false,"gitLfsPath":null,"onBranch":true,"shortPath":"050bd7f","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2FNikNat223%2F30%2Fblob%2Fmaster%2Ftests%2Ftest_all_pets_have_name_age_breed.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"27","truncatedSloc":"21"},"mode":"file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"loggedIn":false,"planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/NikNat223/30/blob/master/tests/test_all_pets_have_name_age_breed.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","releasePath":"/NikNat223/30/releases/new?marketplace=true","showPublishActionBanner":false},"rawBlobUrl":"https://github.com/NikNat223/30/raw/master/tests/test_all_pets_have_name_age_breed.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"symbolsEnabled":true,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"NikNat223","repoName":"30","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timed_out":false,"not_analyzed":false,"symbols":[{"name":"test_there_are_a_name_age_and_gender","kind":"function","ident_start":452,"ident_end":488,"extent_start":448,"extent_end":1748,"fully_qualified_name":"test_there_are_a_name_age_and_gender","ident_utf16":{"start":{"line_number":9,"utf16_col":4},"end":{"line_number":9,"utf16_col":40}},"extent_utf16":{"start":{"line_number":9,"utf16_col":0},"end":{"line_number":27,"utf16_col":0}}}]}},"copilotInfo":null,"copilotAccessAllowed":false,"csrf_tokens":{"/NikNat223/30/branches":{"post":"Id0Q6eQudnGHQgGF4xeapBB0ctjoRXUCbWYXiy1I2h96uf2OEu8bXAYOxynpFP87TAOZ2ysjtyip6OZbmqNegg"},"/repos/preferences":{"post":"BnmbrDo8QGAKFOJ8R7oaaW3gBvixK07Tpi7qtF4ww3yItaJkYybCN3DExLgQgFh4_e1PgUid7pzGisT2jZvyKA"}}},"title":"30/tests/test_all_pets_have_name_age_breed.py at master · NikNat223/30"}