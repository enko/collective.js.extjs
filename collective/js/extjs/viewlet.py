from plone.app.layout.viewlets.common import ViewletBase

EXTJS_LANGUAGES = (
    'af', 'bg', 'ca', 'cs', 'da', 'de', 'el-GR', 'en-GB', 'en',
    'es', 'fa', 'fi', 'fr-CA', 'fr', 'gr', 'he', 'hr', 'hu', 'id',
    'it', 'ja', 'ko', 'lt', 'lv', 'mk', 'nl', 'no-NB', 'no-NN', 'pl', 'pt-BR', 'pt-PT', 'pt',
    'ro', 'ru', 'sk', 'sl', 'sr', 'sr-RS', 'sv-SE', 'th', 'tr', 'ukr', 'vn',
    'zh-CN', 'zh-TW',
)

class ExtLang(ViewletBase):

    def update(self):
        pass

    def render(self):
        return u"""<script url="%s"></script>""" % self.js_lang_url()

    def js_lang_url(self):
        portal_url = self.context.portal_url()
        return "%s/++resource++extjs/locales/ext-lang-%s.js"%(portal_url, self.js_lang())

    def js_lang(self):
        language = self.request.LANGUAGE
        if '-' in language:
            # normalize combined language code
            parts = language.split('-')
            language = "%s_%s" % (parts[0], parts[1].upper())
            if language in EXTJS_LANGUAGES:
                return language
            else:
                # If the combined language doesn't exist in jqueryui
                # check only the first part.
                language = language.split('-')[0]
        if language in EXTJS_LANGUAGES:
            return language
        # Return empty string if the language is not supported
        # by jqueryui so the default this.regional[''] of the datepicker
        # plugin is used.
        return ''
